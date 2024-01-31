import json
import os


def read_jsonl(file_path):
    """读取JSONL文件并返回列表"""
    with open(file_path, 'r') as file:
        return json.loads(file.read())

# 假设你的文件路径列表是 file_paths
def sorted_file():
    file_paths=[]
    for a,b,c in os.walk("./tem_file"):
        for file in c:
            if file.endswith("merged_output.jsonl") and file.startswith("sorted") and "sum" not in file:
                print(file)
                file_paths.append("./tem_file//"+file)
    # file_paths = ['file1.jsonl', 'file2.jsonl', 'file3.jsonl']  # 根据需要修改文件路径
    lists = [read_jsonl(file_path) for file_path in file_paths]
    result = {}
    max_length = max(len(lst) for lst in lists)  # 找到最长的列表长度
    print(max_length)
    for i in range(max_length):
        for lst in lists:
            if i < len(lst):
                if lst[i] != '':
                    result[(lst[i])]=""
    with open("./tem_file/sorted_word_list_sum_merged_output.jsonl","w")as file:
        file.write(json.dumps(list(result.keys())))

def mapped_dict():
    merged_dict = {}
    file_paths=[]
    for a,b,c in os.walk("./tem_file"):
        for file in c:
            if file.endswith("merged_output.jsonl") and file.startswith("final_mapping") and "sum" not in file:
                print(file)
                file_paths.append("./tem_file//"+file)
    # file_paths = ['file1.jsonl', 'file2.jsonl', 'file3.jsonl']  # 根据需要修改文件路径
    lists = [read_jsonl(file_path) for file_path in file_paths]
    for i in lists:
        merged_dict .update(i)
    with open("tem_file/final_mapping_dictsum_merged_output.jsonl", "w")as file:
        file.write(json.dumps((merged_dict)))
# # result 现在包含了从各个列表中抽取的前300个元素
sorted_file()