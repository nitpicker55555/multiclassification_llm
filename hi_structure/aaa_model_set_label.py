import json
import queue
import threading
import torch
# from gpt_api import change_statement
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")
    print("CUDA is not available. Using CPU...")

tokenizer = AutoTokenizer.from_pretrained("bloomberg/KeyBART")
model = AutoModelForSeq2SeqLM.from_pretrained("bloomberg/KeyBART").to(device)
# aa={"label_list": ["GPS privacy breach", "concerns", "senior GPs", "patients", "personal data", "NHS Digital", "doctors" surgeries", "Tower Hamlets", "east London", "patient data", "collection", "refusal", "Health and Social Care Act 2012", "privacy campaigners", "plans", "medical histories", "database", "private sector", "researchers", "NHS Digital", "data", "pseudonymization", "critics", "patients", "medical records", "breach", "collection", "sharing", "personal medical data", "patient awareness", "consent"]}
def one_process(data_queue,lock,file_name,thread_num):
    while True:

        try:
            content,num = data_queue.get(timeout=3)
            # system_content="Please analyze the text provided below and generate labels for it in json format:{'label_list':[]}. The labels should be brief, general, do not exceed two words and consist only of nouns, excluding any adjectives or adverbs or attributive. For consistency across different texts, ensure that similar themes are aligned with similar labels. For example, if the text discusses a new technology in smartphone design, suitable labels might be 'technology', 'smartphones', 'innovation'. If it's about a historical event, labels like 'history', 'politics', 'conflict' might be appropriate. Remember, the labels should be as concise, universal ,and aligned as possible, focusing strictly on nouns. Response in json format:{'label_list':[]}"
            # user_content=content

            result_dict={}
            print(result_dict)

            result_dict['num'] = num
            result_dict['label_list']=with_model(content)


            # result_dict=dict_extract(result_str)

            file_name=str(file_name).replace(".jsonl","")
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
def main_model(file_name,col_nmae):
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
                num_list.append(json_obj['num']) #在标注好的文件中读取已经标注的数据
    except:
        pass
    print("processed_",len(num_list))
    with open(file_name, 'r',encoding='utf-8') as file:
        for num,line in enumerate(file):
            if num in num_list:
                print(num,"processed")
            # 解析每行为 JSON 对象
            print(line)

            json_obj = json.loads(line)

            # 提取 'content' 键的值
            content = json_obj[col_nmae]
            print(content)
            # content = json_obj.get('Overview', None).replace('"Is_relevant": true', "").replace("{", "").replace("}", "")

            # 打印或处理 'content' 的值
            if content not in pre_list and num not in num_list and content!="":

                pre_list.append(content)
                data_queue.put((content,num))

    print("task length",len(pre_list))
    threads = []
    lock = threading.Lock()
    if not data_queue.empty():

        for i in range(1):
            t = threading.Thread(target=one_process, args=(
                data_queue, lock,file_name, i))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()
def with_model(text):

    inputs = tokenizer.encode(text, return_tensors="pt", max_length=512, truncation=True).to(device)
    outputs = model.generate(inputs, max_length=200, num_beams=10, early_stopping=True)
    result=(tokenizer.decode(outputs[0], skip_special_tokens=True))

    return result.split(";")[:-1]
# main_model(r"C:\Users\Morning\Desktop\hiwi\heart\paper\hi_structure\uploads\example.jsonl","content")
# with_model("Tesla is recalling all 363,000 US vehicles with its so-called “Full Self Driving” driver assist software due to safety risks. The National Highway Traffic Safety Administration found that Tesla’s FSD feature led to an unreasonable risk to motor vehicle safety, citing issues with the system's behavior at intersections. Tesla plans to address the issue through an over-the-air software update. There have been 18 reports of incidents related to these conditions, but no reported injuries or deaths. The recall affects all four Tesla models. NHTSA has identified at least 273 crashes involving Tesla’s driver assist systems.")
# main(r"sum_all.xlsx")
# tss()
# print(dict_extract())