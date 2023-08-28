# Splitting the text using the specified delimiter
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
import urllib.request
# URL = "你的网址"  # 替换成你需要访问的网页的URL
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, ElementNotInteractableException
import urllib.request
# URL = "你的网址"  # 替换成你需要访问的网页的URL
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
# 启动Chrome浏览器
# driver = webdriver.Chrome(executable_path=r"C:\Users\Morning\Desktop\hiwi\爬虫\chromedriver.exe")  # 修改为你的chromedriver的实际路径
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=options,executable_path=r"C:\Users\Morning\Desktop\hiwi\爬虫\chromedriver.exe")
# 找到输入框并输入变量a
"""
cd C:\Program Files\Google\Chrome\Application
chrome.exe --remote-debugging-port=9222 --disable-web-security --user-data-dir=remote-profile   
"""

def selenium_spider(order_num,input_str):
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
    order_num =(order_num+ 1)*2
    while True:
        try:
            # print('//*[@id="__next"]/div[1]/div/div/main/div/div[1]/div/div/div/div[%s]/div/div[2]/div[2]/div[2]/button'%(order_num))
            button = driver.find_element(By.XPATH,
                                         '//*[@id="__next"]/div[1]/div/div/main/div/div[1]/div/div/div/div[%s]/div/div[2]/div[2]/div[2]/button'%(order_num))
            button.click()
            break  # 如果点击成功，跳出循环
        except (ElementClickInterceptedException, NoSuchElementException, ElementNotInteractableException) as e:
            # print(f"点击失败: {e}")
            time.sleep(1)  # 等待1秒再次尝试
text = """Proportion of risk to human rights
False: 80.4%
True: 19.6%

Proportion of 
 instances with privacy violations 
 when risk to human rights exist
False: 61.1%
True: 38.9%
-------------------
Proportion of 
 privacy sensitivity 
 when privacy violations occur
Level 2
Some potential damage: 57.1%
Level 3
Routine or Significant Potential Hazard: 28.6%
Level 4
Serious potential hazard: 14.3%
-------------------
Proportion of 
 instances with different severe consequences 
 when privacy violations occur
Level 2
Some potential damage: 42.9%
Level 3
Routine or Significant Potential Hazard: 28.6%
Level 4
Serious potential hazard: 28.6%
-------------------
Proportion of 
 instances with injustice to rights 
 when risk to human rights exist
False: 77.8%
True: 22.2%
-------------------
Proportion of 
 instances with different severity 
 when injustice to rights occur
Level 2
Some potential damage: 53.3%
Level 3
Routine or Significant Potential Hazard: 26.7%
Level 4
Serious potential hazard: 13.3%
Level 5
Unsustainable Potential Damage: 6.7%
-------------------
Proportion of 
 instances involving vulnerable groups 
 when injustice to rights occur
False: 66.7%
True: 33.3% 
-------------------
-------------------
-------------------
Proportion of emotional and psychological harm
False: 73.6%
True: 26.4%

Proportion of 
 vulnerable groups affected 
 when emotional and psychological harm exist
False: 58.3%
True: 41.7%
-------------------
Proportion of 
 cases where harm is reversible 
 when emotional and psychological harm exist
False: 54.2%
True: 45.8%
-------------------
Proportion of 
 affected by challenges to self-identity and values 
 when emotional and psychological harm exist
False: 83.3%
True: 16.7%
-------------------
Proportion of 
 intensity 
 when emotional and psychological harm exist
Level 2
Some potential damage: 45.8%
Level 3
Routine or Significant Potential Hazard: 20.8%
Level 4
Serious potential hazard: 20.8%
Level 5
Unsustainable Potential Damage: 12.5%
-------------------
Proportion of 
 instances where the harm persists 
 when emotional and psychological harm exist
False: 79.2%
True: 20.8%
-------------------
-------------------
-------------------
Proportion of physical harm
False: 67.4%
True: 32.6%
===========
Proportion of 
 severity 
 when physical harm exist
Level 2
Some potential damage: 30.6%
Level 3
Routine or Significant Potential Hazard: 30.6%
Level 4
Serious potential hazard: 24.2%
Level 5
Unsustainable Potential Damage: 14.5%
-------------------
Proportion of 
 instances where the physical harm persists 
 when physical harm exist
False: 50.0%
True: 50.0%
-------------------
Proportion of 
 cases where the physical harm is reversible 
 when physical harm exist
False: 64.5%
True: 35.5%
-------------------
Proportion of 
 instances where the harm is easily detectable 
 when physical harm exist
False: 91.9%
True: 8.1%
-------------------
-------------------
-------------------
Proportion of economic loss
False: 66.3%
True: 33.7%
____________________
Proportion of 
 instances where economic losses persist 
 when economic loss exist
False: 62.3%
True: 37.7%
-------------------
Proportion of 
 the severity of economic impact 
 when economic loss exist
Level 2
Some potential damage: 49.2%
Level 3
Routine or Significant Potential Hazard: 23.0%
Level 4
Serious potential hazard: 21.3%
Level 5
Unsustainable Potential Damage: 6.6%
-------------------
-------------------
-------------------
Proportion of extent of impact is fixed
False: 96.7%
True: 3.3%
____________________
Proportion of 
 affected individuals 
 when extent of impact is fixed
False: 53.9%
True: 46.1%
-------------------
Proportion of 
 affected local population 
 when extent of impact is fixed
False: 56.2%
True: 43.8%
-------------------
Proportion of 
 global implications 
 when extent of impact is fixed
False: 96.6%
True: 3.4%
-------------------
-------------------
-------------------
____________________
Proportion of whether humans can be replaced
False: 37.0%
True: 63.0%
____________________
Proportion of whether there is a law to regulate
False: 3.3%
True: 96.7%
-------------------
-------------------
-------------------
Proportion of ai-based specificity
False: 93.5%
True: 6.5%
____________________
Proportion of 
 cases affected by untimely data training and maintenance 
 when ai-based specificity exist
False: 77.9%
True: 22.1%
-------------------
Proportion of 
 cases affected by opaque and recurring weak capacities 
 when ai-based specificity exist
False: 59.3%
True: 40.7%
-------------------
Proportion of 
 cases affected due to limitations of traditional supervisory methods 
 when ai-based specificity exist
False: 53.5%
True: 46.5%
-------------------
-------------------
-------------------

____________________
Proportion of planning and design
False: 28.3%
True: 71.7%
____________________
Proportion of collection and processing data
False: 44.6%
True: 55.4%
____________________
Proportion of building usage model
False: 77.2%
True: 22.8%
____________________
Proportion of verification and verification
False: 82.6%
True: 17.4%
____________________
Proportion of deployment 
False: 60.9%
True: 39.1%
____________________
Proportion of operation and monitoring
False: 78.3%
True: 21.7%
____________________
Proportion of end user use and impact
False: 30.4%
True: 69.6%
____________________


"""

parts = text.split("-------------------\n-------------------\n-------------------")

print(len(parts
          ))
# for i in parts:
#     print(i+"\n"+"这是关于ai伦理案例库的数据统计，请使用中文分析"+"\n")
answer=[]
def replace_bold(match):
    return "\\textbf{" + match.group(1) + "}"
for num, i in enumerate(parts):
    # if num>=1:
        print(num)
        selenium_spider(num,i + "\n" + "以上数据是关于ai伦理案例库的数据统计，请使用中文进行数据分析,并给出结论与可能的原因")
        time.sleep(1)
        answer.append(pyperclip.paste())
        # print(answer[-1])
        ones = str(pyperclip.paste())
        for i in ones.split("\n"):
            i = i.replace('%', r'\%')
            print(re.sub(r'\*\*(.*?)\*\*', replace_bold, i))
        print("_____________________________________")

    # print(i + "\n" + "这是关于ai伦理案例库的数据统计，请使用中文分析")
    # selenium_spider(num,i + "\n" + "这是关于ai伦理案例库的数据统计，请使用中文分析")
