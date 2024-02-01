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
def find_missing_elements(list1, list2):
    """
    Find elements that are in list1 but not in list2.

    Parameters:
    list1 (list): The first list.
    list2 (list): The second list.

    Returns:
    list: A list of missing elements.
    """
    # Convert list1 to a set to improve lookup time, then find missing elements
    if len(list1)<=len(list2):
        return []

    set1 = set(list1)
    missing_elements = [element for element in set1 if element not in list2]
    return missing_elements

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
def return_time_of_filename(s):
    """
    Extracts and returns the part of the string from the first occurrence of '2'
    to the last occurrence of 'w'.

    :param s: The input string.
    :return: The extracted substring.
    """
    first_2 = s.find('2')
    last_w = s.rfind('w')


    if first_2 == -1 or last_w == -1 or first_2 > last_w:
        return "No valid substring found."

    return s[first_2:last_w-1]
def fill_jsonl_up(folder_path):
    topic_dict={}
    all_content_dict={}
    time_dict = {}
    # 遍历指定文件夹中的所有文件
    for filename_sum in os.listdir(folder_path):
        if "2" in filename_sum:
            topic_name=filename_sum.split("2")[0]
            if topic_name not in topic_dict:
                topic_dict[topic_name]=[]
            topic_dict[topic_name].append(filename_sum)
    # print(topic_dict)
    for topic in topic_dict:
        all_content_dict.update(time_dict)
        time_dict = {}

        for filename_profile in topic_dict[topic]:
            # 检查文件名是否以 "sentiment" 结尾并且是 `.jsonl` 格式
            if filename_profile.endswith("_profile.jsonl"):
                if "sentiment" in filename_profile:
                    print(filename_profile,"========")
                time_in_filename = return_time_of_filename(filename_profile)
                filename_identify = filename_profile.split("_without")[0]
                file_path = os.path.join(folder_path, filename_profile)
                # 打开并读取文件中的每一行
                time_dict[time_in_filename]={}
                with open(file_path, 'r', encoding='utf-8') as file:
                    for num,line in enumerate(file):
                            # 解析 JSON
                            data = json.loads(line)
                            time_dict[time_in_filename][num]=data['content']
        # print(time_dict)
        for filename in os.listdir(folder_path):
            lost_date = 0
            filled_date = 0
            refound_list = 0
            # filename_identify = filename.split("_without")[0]
            # 检查文件名是否以 "sentiment" 结尾并且是 `.jsonl` 格式

            if filename.endswith("sentiment.jsonl"):
                time_in_filename = return_time_of_filename(filename)
                sentiment_dict = {}
                file_path = os.path.join(folder_path, filename)
                # 打开并读取文件中的每一行

                with open(file_path, 'r', encoding='utf-8') as file:
                    for num,line in enumerate(file):
                            # 解析 JSON
                            try:
                                data = json.loads(line)
                            except:
                                print(line)
                            # sentiment_dict
                            sentiment_dict[data['num']]=data['sentiment']
                if time_in_filename not in time_dict:
                    print(time_dict,topic,filename)
                for i in tqdm(time_dict[time_in_filename],desc="process"):
                    if i not in sentiment_dict:
                        same_index_list=find_key_by_value(time_dict[time_in_filename], time_dict[time_in_filename][i])
                        if have_intersection(same_index_list,list(sentiment_dict.keys())):
                            index_shared=find_intersection(same_index_list,list(sentiment_dict.keys()))[0]
                            sentiment_dict[index_shared]=sentiment_dict[index_shared]
                            filled_date+=1
                        else:
                            lost_date += 1
                            # same_index_list = find_key_by_value(time_dict[time_in_filename],
                            #                                     time_dict[time_in_filename][i])
                            # if have_intersection(same_index_list, list(sentiment_dict.keys())):
                            #     refound_list+=1
                with open(file_path.replace(".jsonl","_complete.jsonl"),'w') as file:
                    for s in tqdm(sentiment_dict,desc='write'):
                        file.write(json.dumps({'num':s,'sentiment':sentiment_dict[s]})+"\n")
                print(filename,lost_date,filled_date)
def fill_sentiment_up(path):
    #遍历profile
    profile_dcit={}

    for filename in os.listdir(path):
        # for filename in filename_sum:
            if "2" in filename and filename.endswith("profile.jsonl"):
                key_word=filename.split("20")[0]
                if key_word not in profile_dcit:
                    profile_dcit[key_word]=[]
                profile_dcit[key_word].append(filename)
    for key_word in profile_dcit:
        for filename in profile_dcit[key_word]:
            file_path=path+"\\"+filename
            content_dict = {}
            sentiment_dict={}
            sentiment_ori_dict={}
            sentiment_index=[]
            print(filename,"==========")
            with open(file_path,"r", encoding='utf-8') as file:
                for num, line in enumerate(file):
                    # 解析 JSON
                    data = json.loads(line)

                    content_dict[num] = data['content']
            with open(file_path.replace(".jsonl","_sentiment.jsonl"), "r", encoding='utf-8') as file:
                for num, line in enumerate(file):
                    # 解析 JSON
                    try:
                        data = json.loads(line)
                        # sentiment_index.append(data['num'])
                        sentiment_ori_dict[data['num']]=data['sentiment']
                        sentiment_dict[ content_dict[data['num']]] = data['sentiment']
                    except:
                        print("json error",num)
            print(len(content_dict),len(sentiment_ori_dict))
            missing_indexes=find_missing_elements(list(content_dict.keys()),list(sentiment_ori_dict.keys()))
            missing_number = 0
            if missing_indexes!=[]:

                for missing_index in missing_indexes:
                    missing_content=content_dict[missing_index]
                    try:
                        sentiment_missing_content=sentiment_dict[missing_content]
                        sentiment_ori_dict[missing_index] = sentiment_missing_content
                    except KeyError:
                        # print(missing_index,"missing_content:",missing_content)
                        missing_number+=1
            with open(file_path.replace(".jsonl","_complete.jsonl"),'w') as file:
                for s in tqdm(sentiment_ori_dict,desc='write'):
                    file.write(json.dumps({'num':s,'sentiment':sentiment_ori_dict[s]})+"\n")

            print(len(sentiment_ori_dict),"missing_number",missing_number)
fill_sentiment_up(r"C:\Users\Morning\Desktop\hiwi\heart\paper\hi_structure\twitter_data2")