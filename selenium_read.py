from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
import os
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import urllib.request
import json,re,string
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, ElementNotInteractableException
import urllib.request
# URL = "你的网址"  # 替换成你需要访问的网页的URL
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time
# 启动Chrome浏览器
# driver = webdriver.Chrome(executable_path=r"C:\Users\Morning\Desktop\hiwi\爬虫\chromedriver.exe")  # 修改为你的chromedriver的实际路径
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=options,executable_path=r"C:\Users\Morning\Desktop\hiwi\爬虫\chromedriver.exe")
# 找到输入框并输入变量a

# input_element = driver.find_element(By.XPATH, '//*[@id="prompt-textarea"]')
text_to_send = """
这是第一段文字。

这是第二段文字。

这是第三段文字。
"""
# for ii in text_to_send.split("\n"):
#     input_element.send_keys(ii)  # 你可以替换为变量a的值
# input_element.send_keys("\n")
# 等待按钮变为可用状态并点击
#
# while True:
#     try:
#         button = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div/main/div/div[2]/form/div/div[1]/div/button')
#         button.click()
#         break  # 如果点击成功，跳出循环
#     except (ElementClickInterceptedException, NoSuchElementException, ElementNotInteractableException) as e:
#         print(f"点击失败: {e}")
#         time.sleep(1)  # 等待1秒再次尝试
for num in range(39):
    order_num =(num+ 1)*2
    element_xpath_indication = '//*[@id="__next"]/div[1]/div[2]/div/main/div/div[2]/form/div/div[1]/div/div[2]/div/button/div'
    element_xpath = '//*[@id="__next"]/div[1]/div[2]/div/main/div/div[1]/div/div/div/div[%s]/div/div[2]/div[1]/div/div'%order_num
#//*[@id="__next"]/div[1]/div[2]/div/main/div/div[1]/div/div/div/div[%s]/div/div[2]/div[1]/div/div gpt3

    indication = "generate"
    text=None
    # time.sleep(1)

        # print(indication)
    try:
        # indication = driver.find_element_by_xpath(element_xpath_indication).text
        text = driver.find_element_by_xpath(element_xpath).text

    except:
        pass
    print("__________________________")
    print(num+1)
    print(text)


# button = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div/main/div/div[1]/div/div/div/div[%s]/div/div[2]/div[2]/div[2]/button'%(2))
# button.click()
# print(pyperclip.paste())


