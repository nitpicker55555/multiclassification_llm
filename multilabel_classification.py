import os
import glob,json
import time

import pandas as pd
# 设置你的起始目录
start_directory = '.'
import threading,queue
from gpt_api import change_statement
from jsonstr2json import json_transfer_func
from selenium_chatgpt import selenium_spider
file_num=0
totoal_token=[]

# 遍历所有以 'content_' 开头的文件夹
def one_process(data_queue,overview_column,num_col,folder,excel_file,lock,thread_num):
    run_num = 0
    while True:

        try:
            run_num+=1

            row_num  = data_queue.get(timeout=3)
            send_info=str(overview_column[row_num]).replace('"Is_relevant": true',"")
            if run_num == 1:
                try:

                    # json_result = change_statement(send_info, '', "fine-tune")
                        json_result=selenium_spider(send_info,True)


                except Exception as e:
                    print(thread_num,e)
                    # time.sleep(10)
                    json_result={'Error':True}
                    time.sleep(5)
            else:
                try:

                    # json_result = change_statement(send_info, '', "fine-tune")
                    json_result = selenium_spider(send_info, False)

                except Exception as e:
                    print(thread_num, e)

                    # time.sleep(10)
                    json_result = {'Error': True}
                    time.sleep(5)
                    json_result = selenium_spider(send_info, True)
            specific_num = num_col[row_num]


            print(row_num,specific_num,thread_num,excel_file, json_result)
            json_result = json_result.replace("'", '"').replace('True', 'true').replace('False', 'false')


            try:
                format_json_result = (json_transfer_func(json_result))
            except Exception as e:

                print("error",thread_num,e)
                # data_queue.put((row_num))
                continue
            if not isinstance(format_json_result,dict):
                data_queue.put((row_num))
                continue
            people_labels=['Employee',  'Civilians' ,'Military Personnel','Passenger', 'Pedestrian', 'Driver', 'Government Department', 'Child', 'Customer', 'Tourist', 'Researcher', 'Employer', 'Elderly', 'Athlete', 'Resident', 'Homeless', 'Female', 'SpecificNationalityGroup', 'TrafficParticipant', 'Low-incomeGroup', 'PeopleofColor', 'Male', 'Caucasian', 'SexWorker', 'Student', 'Parent']
            for i in format_json_result['Personnel category']:
                if i not in people_labels:
                    data_queue.put((row_num))
                    continue
            format_json_result['excel_num'] = str(specific_num)
            format_json_result['row_num'] =str(row_num)

            with lock:
                with open(folder + '\\' + excel_file.split("\\")[-1].split(".")[0] + "_multilabel_result_json.jsonl",
                          'a',
                          encoding='utf-8') as f:
                    json_str = json.dumps(format_json_result)
                    f.write(json_str + '\n')
        except queue.Empty:
            print(excel_file, "empty===========")
            with lock:
                with open(folder + '\\' + excel_file.split("\\")[-1].split(".")[0] + "_multilabel_result_json.jsonl",
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
            jsonl_file_path=excel_file.replace(".xlsx","_multilabel_result_json.jsonl")
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

            overview_column = df['Content']
            true_col = df['Relevant']
            num_col = df['num']
            # print(true_col)
            threads = []
            lock = threading.Lock()
            data_queue = queue.Queue()

            # 解析JSONL文件内容

            for row_num, row in enumerate(true_col):
                if row == True and str(num_col[row_num]) not in processed_row_nums and overview_column.isna()[row_num]!=True:
                    processed_row_nums.append(str(num_col[row_num]))
                    data_queue.put((row_num))
            print("data_queue length ",data_queue.qsize(),excel_file)
            print("original length ",len(true_col),excel_file)


            # 排除掉data_queue中已经存在的"row_num"值
            selenium_spider("",False,True) #next_topic
            indication_text="You are a professional journalist. You will label the following news I give you. Each label will be short and broad, please pick the Personnel categories in（Employee, Civilians ,Military Personnel,Passenger, Pedestrian, Driver, Government Department, Child, Customer, Tourist, Researcher, Employer, Elderly, Athlete, Resident, Homeless, Female, Specific Nationality Group, Traffic Participant, Low-income Group, People of Color, Male, Caucasian, Sex Worker, Student, Parent）, nation tags,'News Topics', if it is accident pick 'accident tags' in (Industrial Accidents, Chemical Leakage Accidents, Aviation Accidents, Traffic Accidents, Fire Accidents, Public Accidents, Natural Disasters, Waste of resources, Discrimination, Invasion of Citizens Privacy, Family accident.) if not accident, set 'accident'=false, event cause tags, event consequence tags, output in json format, {'Personnel category' :[],'nation':[],'News Topics':[],'accident tags':[],'event cause':[],'event Consequence':[]}，all of tags you give should be general. if you understand, just say ok"
            selenium_spider(indication_text)
            one_process(data_queue, overview_column, num_col, folder, excel_file, lock,"")
            # for i in range(1):
            #     t = threading.Thread(target=one_process, args=(
            #     data_queue, overview_column, num_col, folder, excel_file, lock, i))
            #     t.start()
            #     threads.append(t)
            #
            # for t in threads:
            #     t.join()




