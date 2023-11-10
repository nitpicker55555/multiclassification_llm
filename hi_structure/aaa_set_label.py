import json
import queue
import threading
import asyncio
from gpt_api import change_statement


# 假设 'your_jsonl_file.jsonl' 是你的 JSONL 文件名


def tss():
    file_name = r'C:\Users\Morning\Desktop\hiwi\gpt_score\twitter_spider\2016-1-1_2016-12-31_without_profile.jsonl'
    file_name = str(file_name).split("\\")[-1].replace(".jsonl", "")
    print(file_name)
# aa={"label_list": ["GPS privacy breach", "concerns", "senior GPs", "patients", "personal data", "NHS Digital", "doctors" surgeries", "Tower Hamlets", "east London", "patient data", "collection", "refusal", "Health and Social Care Act 2012", "privacy campaigners", "plans", "medical histories", "database", "private sector", "researchers", "NHS Digital", "data", "pseudonymization", "critics", "patients", "medical records", "breach", "collection", "sharing", "personal medical data", "patient awareness", "consent"]}
def one_process(data_queue,lock,file_name,thread_num):
    while True:

        try:
            content,num = data_queue.get(timeout=3)
            system_content="Please analyze the text provided below and generate labels for it. The labels should be brief, general, do not exceed two words and consist only of nouns, excluding any adjectives or adverbs or attributive. For consistency across different texts, ensure that similar themes are aligned with similar labels. For example, if the text discusses a new technology in smartphone design, suitable labels might be 'technology', 'smartphones', 'innovation'. If it's about a historical event, labels like 'history', 'politics', 'conflict' might be appropriate. Remember, the labels should be as concise, universal ,and aligned as possible, focusing strictly on nouns. Response in json format:{'label_list':[]}"
            user_content=content
            try:
                result_dict=asyncio.run (change_statement(user_content,system_content))
                print(result_dict)
                if isinstance(result_dict, str):
                    result_dict = json.loads(result_dict)
                result_dict['num'] = num
            except Exception as e:
                print("error and put again, restart ",e)
                data_queue.put(content,num)
                continue
            # result_dict=dict_extract(result_str)

            file_name=str(file_name).split("\\")[-1].replace(".jsonl","")
            with lock:
                with open("%s_labels.jsonl"%file_name,
                          'a',
                          encoding='utf-8') as f:
                    json_str = json.dumps(result_dict)
                    f.write(json_str + '\n')
        except queue.Empty:
                    print( "empty===========", thread_num)

                    break
import pandas as pd

def xlsx_to_json(xlsx_file_path, json_file_path):
    # 读取xlsx文件
    df = pd.read_excel(xlsx_file_path)

    # 打开JSONL文件用于写入
    with open(json_file_path, 'w', encoding='utf-8') as file:
        # 遍历DataFrame的每一行
        for _, row in df.iterrows():
            # 将行转换为JSON格式，并写入文件
            file.write(row.to_json(force_ascii=False) + '\n')
def main(file_name):
    if ".xlsx" in file_name:
        xlsx_to_json(file_name,file_name.replace("xlsx","jsonl"))
        file_name=file_name.replace("xlsx","jsonl")
    data_queue=queue.Queue()
    num_list=[]
    pre_list=[]
    try:
        with open(file_name.replace(".jsonl","_labels.jsonl"), 'r') as file:
            for line in (file):
                json_obj = json.loads(line)
                num_list.append(json_obj['num'])
    except:
        pass
    print("processed_",len(num_list))
    with open(file_name, 'r',encoding='utf-8') as file:
        for num,line in enumerate(file):
            if num in num_list:
                print(num,"processed")
            # 解析每行为 JSON 对象
            json_obj = json.loads(line)

            # 提取 'content' 键的值
            content = json_obj.get('Overview', None).replace(
                    '"Is_relevant": true', "").replace("{", "").replace("}", "")

            # 打印或处理 'content' 的值
            if content not in pre_list and num not in num_list:

                pre_list.append(content)
                data_queue.put((content,num))

    print("task length",len(pre_list))
    threads = []
    lock = threading.Lock()
    if not data_queue.empty():

        for i in range(6):
            t = threading.Thread(target=one_process, args=(
                data_queue, lock,file_name, i))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()
# main(r"sum_all.xlsx")
# tss()
# print(dict_extract())