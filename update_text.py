import pandas as pd
import ast
import re
file_path="case_text.txt"

with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()
next_line=False
line_=[]
sum_line=[]

for line in lines:
    if "___________" in line:
        if len(line_)>1:
            line_str=",".join(line_)
            line_=[]
            print(line_str)
            print("__________")
            sum_line.append(line_str)
        else:
            if len(line_)==1:

                line_str=line_[0]
                line_ = []
                print(line_str)
                print("__________")
                sum_line.append(line_str)

        # print(line_str)
        next_line=True
    else:
        line_.append(line)
existing_file='content.xlsx'
df = pd.read_excel(existing_file)

# 检查'content'列是否存在，如果不存在则创建

# 使用新的列表覆盖'content'列
# 限制长度为较短的那个，以防列表比DataFrame长
min_length = min(len(sum_line), len(df))
df.loc[:min_length-1, 'Content'] = sum_line[:min_length]

# 保存修改后的DataFrame到同一个Excel文件
df.to_excel(existing_file, index=False)