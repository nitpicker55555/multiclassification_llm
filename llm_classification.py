import os
import glob,json
import time

import pandas as pd
# 设置你的起始目录
start_directory = '.'
import threading,queue
from gpt_api import change_statement

file_num=0
totoal_token=[]

# 遍历所有以 'content_' 开头的文件夹
def one_process(data_queue,overview_column,num_col,folder,excel_file,lock,thread_num):
    while True:

        try:
            row_num  = data_queue.get(timeout=3)
            send_info=str(overview_column[row_num]).replace('"Is_relevant": true',"")
            try:
                json_result, each_token = change_statement(send_info, '', "fine-tune")
            except Exception as e:
                print(thread_num,e)
                time.sleep(20)
                json_result, each_token = change_statement(send_info, '', "fine-tune")

            specific_num = num_col[row_num]
            # with open(folder+'\\'+excel_file.split("\\")[-1].split(".")[0]+"classification_result_json.txt",'a',encoding='utf-8') as file:
            #     file.write(json_result)
            #     file.write("___________")
            #     file.write("\n")

            print(row_num,specific_num,thread_num, each_token,excel_file, json_result)
            json_result = json_result.replace("'", '"').replace('True', 'true').replace('False', 'false')


            try:
                format_json_result = json.loads(json_result)
            except Exception as e:

                print(thread_num,e)
                # data_queue.put((row_num))
                break
            format_json_result['excel_num'] = str(specific_num)
            format_json_result['row_num'] =str(row_num)
            format_json_result['each_token'] = str(each_token)
            with lock:
                with open(folder + '\\' + excel_file.split("\\")[-1].split(".")[0] + "classification_result_json.jsonl",
                          'a',
                          encoding='utf-8') as f:
                    json_str = json.dumps(format_json_result)
                    f.write(json_str + '\n')
        except queue.Empty:
            print(excel_file, "empty===========")
            with lock:
                with open(folder + '\\' + excel_file.split("\\")[-1].split(".")[0] + "classification_result_json.jsonl",
                          'a', encoding='utf-8') as f:

                    json_str = json.dumps({'Finish_json_file':True})
                    f.write(json_str + '\n')  # 写入一行并添加换行符
            break


for folder in glob.glob(os.path.join(start_directory, 'content_*')):

    if os.path.isdir(folder):
        print(folder)
        # 在每个 'content_' 文件夹中，查找所有以 'updated_file' 开头的 .xlsx 文件
        for excel_file in (glob.glob(os.path.join(folder, 'updated_file*.xlsx'))):
            processed_row_nums = []
            jsonl_file_path=excel_file.replace(".xlsx","classification_result_json.jsonl")
            if os.path.exists(jsonl_file_path):
                with open(jsonl_file_path, 'r') as f:
                    content = f.read()

                    # 检查是否存在"finish"字符
                if "Finish_json_file"  in content:
                    print(excel_file,"  finished")
                    continue
                else:
                    for line in content.splitlines():
                        data = json.loads(line)
                        if "excel_num" in data:
                            processed_row_nums.append(str(data["excel_num"]))
            df = pd.read_excel(excel_file, engine='openpyxl')

            overview_column = df['Overview']
            true_col = df['Relevant']
            num_col = df['num']
            # print(true_col)
            threads = []
            lock = threading.Lock()
            data_queue = queue.Queue()

            # 解析JSONL文件内容

            for row_num, row in enumerate(true_col):
                if row == True and str(num_col[row_num]) not in processed_row_nums:
                    processed_row_nums.append(str(num_col[row_num]))
                    data_queue.put((row_num))
            print("data_queue length ",data_queue.qsize(),excel_file)
            print("original length ",len(true_col),excel_file)


            # 排除掉data_queue中已经存在的"row_num"值




            for i in range(5):
                t = threading.Thread(target=one_process, args=(
                data_queue, overview_column, num_col, folder, excel_file, lock, i))
                t.start()
                threads.append(t)

            for t in threads:
                t.join()




                    # json_result,each_token=change_statement(overview_column[row_num],'',"fine-tune")
                    # totoal_token+=each_token
                    # specific_num=num_col[row_num]
                    # # with open(folder+'\\'+excel_file.split("\\")[-1].split(".")[0]+"classification_result_json.txt",'a',encoding='utf-8') as file:
                    # #     file.write(json_result)
                    # #     file.write("___________")
                    # #     file.write("\n")
                    #
                    # print(file_num,excel_file,json_result)
                    # print(each_token,totoal_token)
                    # format_json_result=json.loads(json_result)
                    # format_json_result['excel_num']=specific_num
                    # format_json_result['row_num'] = row_num
                    # with open(folder+'\\'+excel_file.split("\\")[-1].split(".")[0]+"classification_result_json.jsonl", 'a',encoding='utf-8') as f:
                    #
                    #         json_str = json.dumps(format_json_result)
                    #         f.write(json_str + '\n')


