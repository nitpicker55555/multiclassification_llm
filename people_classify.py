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
        label_one=[]
        for num,line in enumerate(lines):

            if "人群标签" in line:
                label_one=lines[num+1:]
        for label_ in label_one:

            label_ = re.sub(r'\([^)]*\)', '', label_).strip()
            label_ = re.sub(r'（[^）]*）', '', label_).strip()
            label_=label_.replace("，",",").replace(" ","")
            if "," in label_:
                for label_sub in label_.split(","):
                    if label_sub!="" and label_sub!=" ":
                        if label_sub not in label_dict:
                            label_dict[label_sub]=1
                        else:
                            label_dict[label_sub]+=1
            else:
                if label_ not in label_dict:
                    label_dict[label_] = 1
                else:
                    label_dict[label_] += 1
characters_to_exclude = ["。","，","提到了","宝马","竞争不公平"]
filtered_dict_num={}
print(label_dict)


#{'员工': 14, '乘客': 16, '行人': 6, '司机': 41, '政府部门': 17, '儿童': 1, '顾客/消费者': 11, '旅客/游客': 4, '研究员': 2, '雇主': 1, '老人': 1, '运动员': 3, '居民': 4, '无家可归者': 1, '女性': 2, 'C:\\anaconda\\python.exe C:/Users/Morning/Desktop/hiwi/heart/paper/selenium_read.py': 1, '乘客，女性': 1, '司机，政府部门': 2, '特定国籍人群, 政府部门': 2, '司机, 乘客': 1, '顾客/消费者, 司机': 1, '乘客, 司机, 交通参与者': 1, '乘客, 员工': 1, '政府部门（由于涉及消防车，消防部门可以被认为是政府部门的一部分）': 1, '其他人（这里指的可能是其他驾驶员或路上的行人，但原文并没有明确）': 1, '低收入人群': 1, '有色人种': 2, '男性': 1, '白人': 1, '有色人种，政府部门': 1, '顾客/消费者，男性，女性，有色人种': 1, '顾客/消费者，性工作者': 1, '学生，儿童，居民，政府部门': 1, '研究员，': 1, '有色人种，': 1, '居民,': 3, '低收入人群,': 2, '员工 ,': 1, '有色人种,': 3, '儿童,': 1, '政府部门 ，': 1, '家长': 1}
import matplotlib.pyplot as plt
import numpy as np

# Given dictionary
data_dict ={'Employee': 16,
 'Passenger': 20,
 'Pedestrian': 7,
 'Driver': 46,
 'Government Department': 25,
 'Child': 3,
 'Customer': 14,
 'Tourist': 4,
 'Researcher': 3,
 'Employer': 1,
 'Elderly': 1,
 'Athlete': 3,
 'Resident': 8,
 'Homeless': 1,
 'Female': 4,
 'Specific Nationality Group': 2,
 'Traffic Participant': 1,
 'Low-income Group': 3,
 'People of Color': 8,
 'Male': 2,
 'Caucasian': 1,
 'Sex Worker': 1,
 'Student': 1,
 'Parent': 1}
print(len(data_dict))
# Sort the dictionary by value
sorted_data = dict(sorted(data_dict.items(), key=lambda item: item[1]))

# Extract keys and values
keys = list(sorted_data.keys())
values = list(sorted_data.values())

# Create color gradient based on values
colors = plt.cm.viridis(np.linspace(0, 1, len(values)))

# Plotting

reversed_colors = colors[::-1]

# Plotting with modifications
fig, ax = plt.subplots(figsize=(12, 10))
bars = ax.barh(keys, values, color=reversed_colors)
ax.set_xlabel('Count')
ax.set_title('Classification of people involved in Ai-Cases', fontweight='bold')

# Add colorbar
cbar = plt.colorbar(plt.cm.ScalarMappable(cmap='viridis_r'), ax=ax, orientation='vertical')  # reversed colormap
cbar.set_label('Value Intensity')

# Add text at the bottom left
ax.text(-9, -2, 'Total labels: 24', fontsize=10, va='center', fontweight='bold',ha='left')

plt.tight_layout()
plt.show()