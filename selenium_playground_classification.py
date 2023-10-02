# -*- coding: utf-8 -*-
# Splitting the text using the specified delimiter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
import os
import time
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import urllib.request
import json,re,string
import urllib.request
# URL = "你的网址"  # 替换成你需要访问的网页的URL
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, ElementNotInteractableException
import urllib.request
# URL = "你的网址"  # 替换成你需要访问的网页的URL
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
# 启动Chrome浏览器
# driver = webdriver.Chrome(executable_path=r"C:\Users\Morning\Desktop\hiwi\爬虫\chromedriver.exe")  # 修改为你的chromedriver的实际路径
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9223")
driver = webdriver.Chrome(options=options,executable_path=r"C:\Users\Morning\Desktop\hiwi\爬虫\chromedriver.exe")
# 找到输入框并输入变量a
"""
cd C:\Program Files\Google\Chrome\Application
chrome.exe --remote-debugging-port=9222 --disable-web-security --user-data-dir=remote-profile   
"""
import pandas as pd
def filter_bmp_chars(s):
    return ''.join([c for c in s if ord(c) < 0x10000])
def check_number(path):
    # check if number is 99
    file_path = path

    with open(file_path, 'r',encoding="utf-8") as file:
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
    content_list=[]
    case_text_list=[]
    # final_list=[]
    # 使用os.listdir()列出文件夹中的所有文件和文件夹
    for filename in os.listdir(directory):
        # 使用str.startswith()检查文件名是否以"content"开始
        if filename.startswith("content_"):
            print(filename)
            content_list.append(filename.replace("content_","").replace(".xlsx",""))
    for filename in os.listdir("."):
        # 使用str.startswith()检查文件名是否以"content"开始
        if filename.startswith("case_text_"):
            num_check_result=check_number(filename)
            if num_check_result=="99":
                print(filename,"99 处理结束了")
                case_text_list.append(filename.replace("case_text_","").replace(".txt",""))
            else:
                print(filename,num_check_result)
    print(content_list)
    print(case_text_list)

    final_list=[i for i in content_list if i not in case_text_list]

    return final_list

def get_text(input_str):
    # input_str="在使用特斯拉的自动驾驶模式时，发生了多起不相关的车祸，造成不同程度的伤害。自动驾驶汽车的驾驶能力从完全人为控制到完全自主，允许系统控制速度、方向、加速、减速和变道。在大多数情况下，驾驶员会在碰撞前收到警告，提醒人类驾驶员需要进行干预。"
    input_str=filter_bmp_chars(input_str)
    input_element = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[3]/div[1]/div/div/div[1]/div[2]/textarea')

    # input_element.click()
    driver.execute_script("arguments[0].value = arguments[1];", input_element, "")

    # 计算字符串的长度
    length = len(input_str)

    # 以每次100个字符遍历字符串
    for i in range(0, length, 700):
        # 获取当前位置到下一个100个字符的子字符串
        substring = input_str[i:i + 700]
        input_element.send_keys(substring)  # 你可以替换为变量a的值
        # time.sleep(1)

    btn='//*[@id="root"]/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[3]/div[2]/span/button[1]'
    button = driver.find_element(By.XPATH, btn)
    button.click()

    while True:
        time.sleep(1)
        btn_str='//*[@id="root"]/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[3]/div[2]/span/button[1]/span/span'
        button_text = driver.find_element(By.XPATH, btn_str).text
        if "Submit" in button_text:
            break

    answer_xpath='//*[@id="root"]/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[3]/div[1]/div/div/div/div[2]/textarea'
    ans_text = driver.find_elements(By.XPATH, answer_xpath)
    ans_text_str=ans_text[-1].text
    remove_ = '//*[@id="root"]/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[3]/div[1]/div/div/div/div[3]'
    buttons = driver.find_elements(By.XPATH, remove_)
    buttons[-1].click()

    return (ans_text_str)





def get_test_from_excel(list_):
    res_list=[]
    for i in list_:
        if not pd.isna(i):
            res_list.append(i)
    res="。".join(res_list)
    res="Title:"+res.replace("\n",",")
    return res
# 读取Excel文件
# df = pd.read_excel('Geo-AI ethics cases.xlsx')
#
# # 读取'Description'列
# description_column = df['Description']
# description_column2 = df['Detailed Description']
# description_column1=df['Title']
def get_text_from_txt(txt_name):

    file_path = 'case_text_%s.txt'%txt_name

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

def one_iteration(num_check,search_name):
    # search_name=''

    df = pd.read_excel(r"C:\Users\Morning\Desktop\hiwi\case_spider\content_%s.xlsx"%search_name)

    description_column2 = df['Content']
    description_column1=df['Title']
    # print(df.shape[0])
    """
    Given a news text, provide the following fields in a JSON dict, where applicable:Risk to Human Rights,instances with privacy violations,privacy sensitivity,privacy violations severity,instances with injustice to rights,Severity of injustice,instances involving vulnerable groups,emotional and psychological harm,vulnerable groups affected,cases where harm is reversible,affected by challenges to self-identity and values,Severity of emotional and psychological harm,instances where the harm persists,Physical harm,Severity of Physical harm ,instances where the physical harm persists,cases where the physical harm is reversible,instances where the harm is easily detectable,Economic loss,instances where economic losses persist,the severity of economic impact,extent of impact is fixed,affected individuals,affected local population,global implications,Whether humans can be replaced,Whether there is a law to regulate,AI-based specificity,cases affected by untimely data training and maintenance,cases affected by opaque and recurring weak capacities,cases affected due to limitations of traditional supervisory methods,lifecycle time period-planning and design,lifecycle time period-collection and processing data,lifecycle time period-building usage model,lifecycle time period-verification and verification,lifecycle time period-deployment ,lifecycle time period-Operation and Monitoring,lifecycle time period-End User Use and Impact,Geographical Attributes-Timeliness,Geographical Attributes-Accuracy,Data Production Process -Acquisition,Data Production Process-Preprocessing,Data Production Process-Integration,Data Production Process-Storage and Management,Data Production Process-Analysis and Processing,Data Production Process-Application Communication
    
    Based on the news information provided, please determine whether the news is about a specific single case. If so, extract the specific information about the case. If not, simply output "Not a single case news"
    
    Based on the news information provided, please determine whether the news is about autonomous driving privacy leakage. If so, extract the specific information about the case. If not, simply output "Not relevant news"
    tem2 top p 0.2
    """
    # cases=get_text_from_txt(search_name)
    for i in range(df.shape[0]):
    # for i in range(1):
        if i>=num_check:

            res=get_test_from_excel([description_column1[i],description_column2[i]])
            print(res)
            # res= cases[i]
            if "Not a single accident news" not in res:
                print(i,"__________________________________________________")
                playgorund_feedback=get_text(res)
                print(playgorund_feedback)
                with open("case_text_%s.txt"%search_name,'a',encoding='utf-8') as filewrite:
                    filewrite.write(str(i) + "__________________________________________________" + '\n')
                    filewrite.write(playgorund_feedback+ '\n')
                time.sleep(1)
def input_system_str(input_str):
    xpath_str='//*[@id="root"]/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div/div[2]/textarea'
    textarea = driver.find_element_by_xpath(
        xpath_str)

    # 清空<textarea>元素
    textarea.clear()
    textarea.send_keys(input_str)
# //*[@id="root"]/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div/div[2]/textarea

process_list=\
    file_check(r"C:\Users\Morning\Desktop\hiwi\case_spider")
print(len(process_list))
print(process_list)

for num,i in enumerate(process_list):
    try:
        num_check=int(check_number(i))
    except:
        num_check=0
    print(num,i,"____________________ processing")

    input_system_str("""
    Based on the news information provided, please determine whether the news is about %s. If so, extract the specific information about the case. If not, simply output "Not relevant news"
    """%(i.replace("_"," ")))
    one_iteration(num_check,i)