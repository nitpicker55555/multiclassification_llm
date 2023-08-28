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

input_element = driver.find_element(By.XPATH, '//*[@id="prompt-textarea"]')
text_to_send = """
这是第一段文字。

这是第二段文字。

这是第三段文字。
"""
for ii in text_to_send.split("\n"):
    input_element.send_keys(ii)  # 你可以替换为变量a的值
# input_element.send_keys("\n")
# 等待按钮变为可用状态并点击
#
element_xpath = '//*[@id="__next"]/div[1]/div[2]/div/main/div/div[1]/div/div/div/div[4]/div/div[2]/div[1]/div/div/p'

text = None
while text is None:
    try:
        text = driver.find_element_by_xpath(element_xpath).text
        print(text)
    except NoSuchElementException:
        print("Element not found. Retrying...")
        time.sleep(5)  # 设置一个间隔时间，例如5秒，避免过于频繁的查询

# def replace_bold(match):
#     return "\\textbf{" + match.group(1) + "}"
#
# # for num in range(8):
# num=18
# while True:
#     try:
#         button = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div/main/div/div[1]/div/div/div/div[%s]/div/div[2]/div[2]/div[2]/button'%num)
#         button.click()
#         break  # 如果点击成功，跳出循环
#     except (ElementClickInterceptedException, NoSuchElementException, ElementNotInteractableException) as e:
#         # print(f"点击失败: {e}")
#         time.sleep(1)  # 等待1秒再次尝试
# ones=str(pyperclip.paste())
# for i in ones.split("\n"):
#     i=i.replace('%', r'\%')
#     print(re.sub(r'\*\*(.*?)\*\*', replace_bold, i))
#
# print("_____________________________________")



