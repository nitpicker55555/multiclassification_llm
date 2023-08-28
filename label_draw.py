import re
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
# Read the file
with open(r"C:\Users\Morning\Desktop\gpt4分类.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Split the content by the case separator
cases = content.split("__________________________")

# Extract accident tags from each case
accident_tags = []
for case in cases:
    match = re.search(r'事故标签：(.+)', case)
    if match:
        accident_tags.extend(match.group(1).split('，'))

# Count the frequency of each accident tag
accident_tag_count = defaultdict(int)
for tag in accident_tags:
    accident_tag_count[tag.strip()] += 1

# Extract accident tags based on the new understanding
accident_tags_updated = []
for case in cases:
    match = re.search(r'事故标签：\n(.+?)\n人群标签：', case, re.DOTALL)
    if match:
        accident_tags_updated.extend([tag.strip() for tag in match.group(1).split("\n") if tag.strip()])

# Count the frequency of each accident tag
accident_tag_count_updated = defaultdict(int)
for tag in accident_tags_updated:
    # accident_tag_count_updated[tag] += 1
    tag=tag.replace(",","，")
    tag = tag.replace(" ", "")
    tag=re.sub(r'\([^)]+\)', '', tag)

    if "，" in tag:
        tag_list=tag.split("，")
        print(tag)
        for tag in tag_list:
            if tag!="":
                accident_tag_count_updated[tag] += 1
    else:
        # print(tag)
        accident_tag_count_updated[tag] += 1
accident_tag_dict={'Industrial Accidents': 3, 'Chemical Leakage Accidents': 1, 'Aviation Accidents': 2, 'Traffic Accidents': 60, 'Fire Accidents': 1, 'Public Accidents': 7, 'Natural Disasters': 3, 'Waste of resources': 3, 'Discrimination': 14, 'Undermining social equity': 18, 'Nationality discrimination': 2, 'Racial discrimination': 8, 'Sex discrimination': 1, 'Family accident': 1 }
print(sum(accident_tag_count_updated.values()))
print(accident_tag_count_updated)
keys = accident_tag_dict.keys()
values = accident_tag_dict.values()

sorted_data = {k: v for k, v in sorted(accident_tag_dict.items(), key=lambda item: item[1], reverse=True)}

# 创建渐变色
colors = plt.cm.viridis(np.linspace(0, 1, len(sorted_data)))

# 绘制条形图
plt.bar(sorted_data.keys(), sorted_data.values(), color=colors)
plt.xticks(rotation=45, ha='right')  # 使x轴标签倾斜45度
plt.tight_layout()  # 确保标签不会重叠
# 添加标题和标签
plt.title('Type of accident')
plt.xlabel('Accidents')
plt.ylabel('Count')

# 显示图
plt.show()




