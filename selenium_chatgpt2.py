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
import json, re, string
import urllib.request
# URL = "你的网址"  # 替换成你需要访问的网页的URL
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, \
    ElementNotInteractableException
import urllib.request
# URL = "你的网址"  # 替换成你需要访问的网页的URL
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

# 启动Chrome浏览器
# driver = webdriver.Chrome(executable_path=r"C:\Users\Morning\Desktop\hiwi\爬虫\chromedriver.exe")  # 修改为你的chromedriver的实际路径
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\Morning\Desktop\hiwi\爬虫\chromedriver.exe")
# 找到输入框并输入变量a
"""
cd C:\Program Files\Google\Chrome\Application
chrome.exe --remote-debugging-port=9222 --disable-web-security --user-data-dir=remote-profile   
"""


def selenium_spider(input_str):
    input_element = driver.find_element(By.XPATH, '//*[@id="prompt-textarea"]')
    for ii in input_str.split("\n"):
        input_element.send_keys(ii)  # 你可以替换为变量a的值
    input_element.send_keys('\n')
    # 等待按钮变为可用状态并点击

    # while True:
    #     try:
    #         button = driver.find_element(By.XPATH,
    #                                      '//*[@id="__next"]/div[1]/div/div/main/div/div[2]/form/div/div[1]/div/button')
    #         button.click()
    #         break  # 如果点击成功，跳出循环
    #     except (ElementClickInterceptedException, NoSuchElementException, ElementNotInteractableException) as e:
    #         print(f"点击失败: {e}")
    #         time.sleep(1)  # 等待1秒再次尝试
    # order_num =(order_num+ 1)*2
    element_xpath_indication = '//*[@id="__next"]/div[1]/div[2]/div/main/div/div[2]/form/div/div[1]/div/div[2]/div/button/div'
    xpath_str = '//*[@id="__next"]/div[1]/div/div/main/div/div[1]/div/div/div/div/div/div/div[2]/div[1]/div/div'

    # //*[@id="__next"]/div[1]/div gpt3
    # //*[@id="__next"]/div[1]/div[2] gpt4
    indication = "generate"
    text = None
    time.sleep(1)
    while indication != "Regenerate":
        # print(indication)
        try:
            elements = driver.find_elements_by_xpath(xpath_str)
            text = elements[-1].text
            indication = driver.find_element_by_xpath(element_xpath_indication).text


        except (NoSuchElementException, StaleElementReferenceException) as e:
            # print("Element not found. Retrying...")
            time.sleep(1)  # 设置一个间隔时间，例如5秒，避免过于频繁的查询
    # print(element_xpath)

    print(text)
    return text


answer = []
import pandas as pd

# 读取.xlsx文件
file_path = 'Geo-AI ethics cases(1).xlsx'
df = pd.read_excel(file_path, engine='openpyxl')

# 创建一个空列表存放提取的数据
data_list = []

# 通过行迭代，提取每行的 '标题列'、'说明列' 和 '详细描述列' 的数据
for _, row in df.iterrows():
    title = row['标题']
    description = row['说明']
    details = row['详细描述']

    # 将这三个数据元素添加到一个新的列表中
    data_list.append(str([title, description, details]).replace("nan", ""))
# list_second=['3', '4', '5', '6', '7', '8', '9', '10', '13', '14', '15', '16', '18', '19', '20', '21', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '40', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '57', '58', '59', '60', '61', '63', '64', '65', '66', '67', '68', '69', '70', '71']
# list_second = ['64', '65', '66', '67', '68', '69', '70', '71']
# list_exclude = ['40', '38', '48']
num_true = 0
for num, i in enumerate(data_list):
    # if str(num) in list_second and str(num) not in list_exclude:
        if num>=49:
            num_true += 1
            print(num)

            ans = selenium_spider(
                i + "\n" + "")

            time.sleep(1)
            answer.append(ans)
            # print(answer[-1])
            print("_____________________________________")

    # print(i + "\n" + "这是关于ai伦理案例库的数据统计，请使用中文分析")
    # selenium_spider(num,i + "\n" + "这是关于ai伦理案例库的数据统计，请使用中文分析")
