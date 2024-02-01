
import json
import queue
import threading
import logging
import torch
from tqdm import tqdm
from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
import numpy as np
from scipy.special import softmax
# from gpt_api import change_statement
logging.getLogger("transformers.modeling_utils").setLevel(logging.ERROR)

if torch.cuda.is_available():
    device = torch.device("cuda")
    print("CUDA is available. Using GPU...")
else:
    device = torch.device("cpu")
    print("CUDA is not available. Using CPU...")


# aa={"label_list": ["GPS privacy breach", "concerns", "senior GPs", "patients", "personal data", "NHS Digital", "doctors" surgeries", "Tower Hamlets", "east London", "patient data", "collection", "refusal", "Health and Social Care Act 2012", "privacy campaigners", "plans", "medical histories", "database", "private sector", "researchers", "NHS Digital", "data", "pseudonymization", "critics", "patients", "medical records", "breach", "collection", "sharing", "personal medical data", "patient awareness", "consent"]}
def one_process(data_queue,lock,file_name,thread_num,pbar):
    while True:

        try:
            content,num = data_queue.get(timeout=3)
            # system_content="Please analyze the text provided below and generate labels for it in json format:{'label_list':[]}. The labels should be brief, general, do not exceed two words and consist only of nouns, excluding any adjectives or adverbs or attributive. For consistency across different texts, ensure that similar themes are aligned with similar labels. For example, if the text discusses a new technology in smartphone design, suitable labels might be 'technology', 'smartphones', 'innovation'. If it's about a historical event, labels like 'history', 'politics', 'conflict' might be appropriate. Remember, the labels should be as concise, universal ,and aligned as possible, focusing strictly on nouns. Response in json format:{'label_list':[]}"
            # user_content=content

            result_dict={}

            result_dict['num'] = num
            result_dict['sentiment']=str(with_model(content))
            # print(result_dict)


            # result_dict=dict_extract(result_str)

            file_name=str(file_name).replace(".jsonl","")
            with lock:
                with open("%s_sentiment.jsonl"%file_name,
                          'a',
                          encoding='utf-8') as f:
                    json_str = json.dumps(result_dict)
                    f.write(json_str + '\n')
                pbar.update(1)
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
def sentiment_model(file_name,col_nmae,thread_num):
    if ".xlsx" in file_name:
        xlsx_to_json(file_name,file_name.replace("xlsx","jsonl"))
        file_name=file_name.replace("xlsx","jsonl")
    data_queue=queue.Queue()
    num_list=[]
    pre_list=[]
    try:
        with open(file_name.replace(".jsonl","_sentiment.jsonl"), 'r') as file:
            for line in (file):
                json_obj = json.loads(line)
                num_list.append(json_obj['num']) #在标注好的文件中读取已经标注的数据
    except:
        pass
    print("processed_",len(num_list))
    with open(file_name, 'r',encoding='utf-8') as file:
        for num,line in enumerate(file):
            # if num in num_list:
            #     print(num,"processed")
            # 解析每行为 JSON 对象
            # print(line)

            json_obj = json.loads(line)

            # 提取 'content' 键的值
            content = json_obj[col_nmae]
            # print(content)
            # content = json_obj.get('Overview', None).replace('"Is_relevant": true', "").replace("{", "").replace("}", "")

            # 打印或处理 'content' 的值
            if content not in pre_list and num not in num_list and content!="":

                pre_list.append(content)
                data_queue.put((content,num))

    print("task length",len(pre_list))
    threads = []
    lock = threading.Lock()
    pbar = tqdm(total=data_queue.qsize())

    def thread_target(data_queue, lock, file_name, thread_id, pbar):
        one_process(data_queue, lock, file_name, thread_id, pbar)


    if not data_queue.empty():

        for i in range(thread_num):
            t = threading.Thread(target=thread_target, args=(
                data_queue, lock,file_name, i, pbar))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()
    pbar.close()  # 关闭进度条
def with_model(text):
    def preprocess(text):
        new_text = []
        for t in text.split(" "):
            t = '@user' if t.startswith('@') and len(t) > 1 else t
            t = 'http' if t.startswith('http') else t
            new_text.append(t)
        return " ".join(new_text)

    MODEL = f"cardiffnlp/twitter-roberta-base-sentiment-latest"
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    config = AutoConfig.from_pretrained(MODEL)
    # PT
    model = AutoModelForSequenceClassification.from_pretrained(MODEL).to(device)
    # model.save_pretrained(MODEL)
    # text = "Covid cases are increasing fast!"
    text = preprocess(text)
    encoded_input = tokenizer(text, return_tensors='pt').to(device)
    output = model(**encoded_input)
    scores = output[0][0].detach()  # 仍然在 GPU 上
    scores = torch.softmax(scores, dim=0)  # 在 GPU 上执行 softmax

    ranking = np.argsort(scores.cpu().numpy())
    ranking = ranking[::-1]
    l = config.id2label[ranking[0]]
    s = scores[ranking[0]]

    return {l:s}
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Example Script with Named Arguments')


    parser.add_argument('--file_path', type=str, help='file_path')
    parser.add_argument('--col_name', type=str, help='col_name')
    parser.add_argument('--processes_num', type=int, help='processes_num')
    # parser.add_argument('--max_out_put_length', type=int, help='max_out_put_length')
    # parser.add_argument('--num_beams', type=int, help='num_beams')
    args = parser.parse_args()

    if args.col_name==None:
        args.col_name="content"
    if args.processes_num==None:
        args.processes_num=8
    sentiment_model(args.file_path,args.col_name,args.processes_num)
# sentiment_model(r"/content/Ethical AI2019-1-1_2019-5-31_without_profile.jsonl","content")