import os
from tqdm import tqdm
import json
from datetime import datetime
def find_key_by_value(dictionary, target_value):
    """
    Function to find the key(s) corresponding to a given value in a dictionary.

    :param dictionary: The dictionary to search.
    :param target_value: The value for which the key(s) are to be found.
    :return: A list of keys that correspond to the target value.
    """
    keys_with_target_value = [key for key, value in dictionary.items() if value == target_value]
    return keys_with_target_value
def have_intersection(list1, list2):
    """
    Function to determine if two lists have any common elements (intersection).

    :param list1: The first list.
    :param list2: The second list.
    :return: True if there is any common element, False otherwise.
    """
    # Convert lists to sets and check if intersection is non-empty
    set1 = set(list1)
    set2 = set(list2)
    return not set1.isdisjoint(set2)
def find_intersection(list1, list2):
    """
    Function to find the intersection (common elements) of two lists.

    :param list1: The first list.
    :param list2: The second list.
    :return: A list of elements that are common in both lists.
    """
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1.intersection(set2)
    return list(intersection)
def fill_jsonl_up(folder_path):
    time_dict={}

    # 遍历指定文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 检查文件名是否以 "sentiment" 结尾并且是 `.jsonl` 格式
        if filename.endswith("_profile.jsonl"):
            file_path = os.path.join(folder_path, filename)
            # 打开并读取文件中的每一行
            time_dict[filename.split("_without")[0]]={}
            with open(file_path, 'r', encoding='utf-8') as file:
                for num,line in enumerate(file):
                        # 解析 JSON
                        data = json.loads(line)
                        time_dict[filename.split("_without")[0]][num]=data['content']
    for filename in os.listdir(folder_path):
        # 检查文件名是否以 "sentiment" 结尾并且是 `.jsonl` 格式
        if filename.endswith("sentiment.jsonl"):
            sentiment_dict = {}
            file_path = os.path.join(folder_path, filename)
            # 打开并读取文件中的每一行

            with open(file_path, 'r', encoding='utf-8') as file:
                for num,line in enumerate(file):
                        # 解析 JSON
                        data = json.loads(line)
                        # sentiment_dict
                        sentiment_dict[data['num']]=data['sentiment']
            for i in tqdm(time_dict[filename.split("_without")[0]],desc="process"):
                if i not in sentiment_dict:
                    same_index_list=find_key_by_value(time_dict[filename.split("_without")[0]], time_dict[filename.split("_without")[0]][i])
                    if have_intersection(same_index_list,list(sentiment_dict.keys())):
                        index_shared=find_intersection(same_index_list,list(sentiment_dict.keys()))[0]
                        sentiment_dict[i]=sentiment_dict[index_shared]
                    else:
                        print(i,"content:",time_dict[filename.split("_without")[0][i]])
            with open(file_path.replace(".jsonl","_complete.jsonl"),'w') as file:
                for s in tqdm(sentiment_dict,desc='write'):
                    file.write(json.dumps({'num':s,'sentiment':sentiment_dict[s]})+"\n")
fill_jsonl_up(r"C:\Users\Morning\Desktop\hiwi\heart\paper\hi_structure\twitter_files")