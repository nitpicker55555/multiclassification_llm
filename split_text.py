# -*- coding: utf-8 -*-
import re

with open(r"C:\Users\Morning\Desktop\gpt4分类.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Split the content by the specified delimiter
cases = content.split("__________________________")

# Extract case numbers and accident labels
case_numbers = []
missing_labels = []
label_is_none = []
label_list=[]
label_dict={}
for case in cases:
    lines = case.strip().split("\n")
    if len(lines) > 1:  # Check if there is more than just the case number
        case_number = lines[0]
        case_numbers.append(case_number)
        label_one=None
        for line in lines:

            list_=['驾驶员过分依赖技术导致的注意力分散', '驾驶员操作问题', '除驾驶员外的人为因素', 'AI的决策制定缺陷', '路径规划问题', '紧急响应问题', '传感器或数据输入错误', '数据处理错误', '响应时延问题', '训练数据和验证问题', '硬件或软件故障', '系统集成和硬件问题', '控制与执行问题', '人机交互问题', '透明性与可解释性问题', '通讯和交互问题', '对乘客造成安全威胁', '对乘客外的他人造成安全威胁', '系统的鲁棒性和容错能力问题', '反馈机制不足', '数据不准确或不完整']
            for item_ in list_:
                if item_ in line:
                    label_one = item_
                    if label_one not in label_dict and label_one != None:
                            label_dict[label_one] = []
                            print(label_one)
                            label_dict[label_one].append(case_number)
                    else:
                            label_dict[label_one].append(case_number)
characters_to_exclude = ["。","，","提到了","宝马","竞争不公平"]
filtered_dict_num={}
# 删除键包含特定字符的项
filtered_dict = {key: value for key, value in label_dict.items() if all(char not in key for char in characters_to_exclude)}
print(filtered_dict)
print(len(filtered_dict))
print(filtered_dict.keys())
for i in filtered_dict:
    filtered_dict_num[i]=len(filtered_dict[i])
print(sum(filtered_dict_num.values()))
print(len(case_numbers))