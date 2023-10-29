# -*- coding: utf-8 -*-

import os
import time

import urllib.request
import json, re, string
import urllib.request
# URL = "你的网址"  # 替换成你需要访问的网页的URL
import random

from selenium_chatgpt import selenium_spider
# # driver = webdriver.Chrome(executable_path=r"C:\Users\Morning\Desktop\hiwi\爬虫\chromedriver.exe")  # 修改为你的chromedriver的实际路径
# options = Options()
# options.add_experimental_option("debuggerAddress", "127.0.0.1:9223")
# driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\Morning\Desktop\hiwi\爬虫\chromedriver.exe")
# # 找到输入框并输入变量a
"""
cd C:\Program Files\Google\Chrome\Application
chrome.exe --remote-debugging-port=9222 --disable-web-security --user-data-dir=remote-profile   
"""
import pandas as pd


def filter_bmp_chars(s):
    return ''.join([c for c in s if ord(c) < 0x10000])
def check_file_finish(path):
    def contains_string(filename, target_string):
        with open(filename, 'r', encoding="utf-8") as file:
            content = file.read()
            return target_string in content

    filename = path
    if contains_string(filename, "case_text_end"):
        return True
    else:
        return False

def check_number(path):
    # check if number is 99
    file_path = path

    with open(file_path, 'r', encoding="utf-8") as file:
        content = file.read()

    # Define the pattern to search for the last occurrence of "____...____" and the number to its left
    pattern = re.compile(r'(\d+)_{2,}')

    # Find all occurrences of the pattern in the content
    matches = pattern.findall(content)

    # Get the last matched number if any matches were found
    last_number = (matches[-1]) if matches else None
    return last_number


def file_check(path):
    # 指定文件夹路径，例如当前文件夹
    directory = path
    content_list = []
    case_text_list = []
    # final_list=[]
    # 使用os.listdir()列出文件夹中的所有文件和文件夹
    for filename in os.listdir(directory):
        # 使用str.startswith()检查文件名是否以"content"开始
        if filename.startswith("content_") and ".xlsx" in filename:
            print(filename)
            content_list.append(filename.replace("content_", "").replace(".xlsx", ""))
    for folder in os.listdir(os.getcwd()):
        if folder.startswith('content_') and os.path.isdir(folder):

            folder_path = os.path.join(os.getcwd(), folder)
            count = 0
            num_cases = 0
            # 遍历文件夹中的每个txt文件
            for filename in os.listdir(folder_path):
                if filename.startswith("case_text_"):

                    num_check_result = check_number(folder_path+'/'+filename)
                    check_finish=check_file_finish(folder_path+'/'+filename)
                    if check_finish:
                        print(filename, num_check_result,"= 处理结束了")
                        case_text_list.append(filename.replace("case_text_", "").replace(".txt", ""))
                    else:
                        print(filename, num_check_result)
    print(content_list)
    print(case_text_list)

    final_list = [i for i in content_list if i not in case_text_list]

    return final_list


def get_text_from_excel(list_):
    res_list = []
    for i in list_:
        if not pd.isna(i):
            res_list.append(i)

    res = "。".join(res_list)
    res = "Title:" + res.replace("\n", ",")
    return res


# 读取Excel文件
# df = pd.read_excel('Geo-AI ethics cases.xlsx')
#
# # 读取'Description'列
# description_column = df['Description']
# description_column2 = df['Detailed Description']
# description_column1=df['Title']
def get_text_from_txt(txt_name):
    file_path = 'case_text_%s.txt' % txt_name

    # Read the file to check its contents
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    cases = extract_cases(lines)
    return cases


# Function to extract individual cases from the text file
def extract_cases(lines):
    cases = []
    current_case = ""
    for line in lines:
        if line.strip().endswith("__________________________________________________"):
            if current_case:
                cases.append(current_case.strip())
            current_case = ""
        else:
            current_case += line
    if current_case:
        cases.append(current_case.strip())
    return cases


# Extract cases from the lines read from the file

def one_iteration(num_check, search_name):
    # search_name=''

    df = pd.read_excel(r"C:\Users\Morning\Desktop\hiwi\case_spider\case\content_%s.xlsx" % search_name)

    description_column2 = df['Content']
    description_column1 = df['Title']
    # print(df.shape[0])
    """
    Given a news text, provide the following fields in a JSON dict, where applicable:Risk to Human Rights,instances with privacy violations,privacy sensitivity,privacy violations severity,instances with injustice to rights,Severity of injustice,instances involving vulnerable groups,emotional and psychological harm,vulnerable groups affected,cases where harm is reversible,affected by challenges to self-identity and values,Severity of emotional and psychological harm,instances where the harm persists,Physical harm,Severity of Physical harm ,instances where the physical harm persists,cases where the physical harm is reversible,instances where the harm is easily detectable,Economic loss,instances where economic losses persist,the severity of economic impact,extent of impact is fixed,affected individuals,affected local population,global implications,Whether humans can be replaced,Whether there is a law to regulate,AI-based specificity,cases affected by untimely data training and maintenance,cases affected by opaque and recurring weak capacities,cases affected due to limitations of traditional supervisory methods,lifecycle time period-planning and design,lifecycle time period-collection and processing data,lifecycle time period-building usage model,lifecycle time period-verification and verification,lifecycle time period-deployment ,lifecycle time period-Operation and Monitoring,lifecycle time period-End User Use and Impact,Geographical Attributes-Timeliness,Geographical Attributes-Accuracy,Data Production Process -Acquisition,Data Production Process-Preprocessing,Data Production Process-Integration,Data Production Process-Storage and Management,Data Production Process-Analysis and Processing,Data Production Process-Application Communication

    Based on the news information provided, please determine whether the news is about a specific single case. If so, extract the specific information about the case. If not, simply output "Not a single case news"

    Based on the news information provided, please determine whether the news is about autonomous driving privacy leakage. If so, extract the specific information about the case. If not, simply output "Not relevant news"
    tem2 top p 0.2
    """
    # cases=get_text_from_txt(search_name)
    case_num=0
    for i in range(df.shape[0]):
        # for i in range(1):
        if i ==(df.shape[0]-1):
            with open("case_text_%s.txt" % search_name, 'a', encoding='utf-8') as filewrite:
                filewrite.write(str('case_text_end') + "=======" + '\n')
        if i >= num_check:
            if str(description_column1[i]) !="nan":
                # print(description_column2[i],"不空")
                case_num+=1

                res = get_text_from_excel([description_column1[i], description_column2[i]])
                print(res)
                # res= cases[i]

                print(i, "__________________________________________________")



                if case_num==1:
                    try:
                        playgorund_feedback = selenium_spider(res,True)
                    except Exception as e:
                        playgorund_feedback="'Is_relevant'=False,True mode error"
                        print("True mode error",e)
                else:
                    try:
                        playgorund_feedback = selenium_spider(res, False)
                    except Exception as e:
                        print("False mode error, now try True mode", e)
                        try:
                            playgorund_feedback = selenium_spider(res, True)
                        except:

                            playgorund_feedback = "'Is_relevant'=False,False mode error"
                            print("False mode error", e)

                print(playgorund_feedback)
                if "Is_relevant" not in playgorund_feedback:
                    playgorund_feedback="'Is_relevant'=False "+ playgorund_feedback
                with open("case_text_%s.txt" % search_name, 'a', encoding='utf-8') as filewrite:
                    filewrite.write(str(i) + "__________________________________________________" + '\n')
                    filewrite.write(playgorund_feedback + '\n')
                sleep_time = random.uniform(1, 3)
                time.sleep(sleep_time)
            else:
                print(i,"行为空",description_column1[i])
                with open("case_text_%s.txt" % search_name, 'a', encoding='utf-8') as filewrite:
                    filewrite.write(str(i) + "__________________________________________________" + '\n')
                    filewrite.write("'Is_relevant'=False" + '\n')



# //*[@id="root"]/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div/div[2]/textarea

process_list = \
    file_check(r"C:\Users\Morning\Desktop\hiwi\case_spider\case")
print(len(process_list))
print(process_list)

for num, i in enumerate(process_list):
    try:
        num_check = int(check_number("case_text_"+i+".txt"))
    except:
        num_check = 0

    selenium_spider("",False,True)
    sleep_time = random.uniform(2, 3)
    time.sleep(sleep_time)
    print("process_list number: ",num, "num_check: ",num_check,i, "____________________ processing")
    # indication_str = ("""I will send you a piece of news,your answer need to be json format which has two keys{'Is_relevant','Specific_information'}
    # please determine whether the news is about %s. If so, tell me why this news fits %s and the part of this news that fits %s as detailed as possible and output {'Is_relevant'=True,'Specific_information'= (specific information as detailed as possible)}, If not, {'Is_relevant'=False,'Specific_information'=None}. if you understand, please simply answer "ok".
    # """ % (i.replace("_", " "),i.replace("_", " "),i.replace("_", " ")))
    indication_str = ("""I will send you a piece of news,your answer need to be json format which has two keys{'Is_relevant','Specific_information'}
    please determine whether the news is about Problems caused by maps or geographical information. If so, tell me why this news fits and the part of this news that fits as detailed as possible and output {'Is_relevant'=True,'Specific_information'= (specific information as detailed as possible)}, If not, {'Is_relevant'=False,'Specific_information'=None}. if you understand, please simply answer "ok".""")

    print(selenium_spider(indication_str))

    one_iteration(num_check, i)