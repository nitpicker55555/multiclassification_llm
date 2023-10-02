import pandas as pd
import ast
import re

def to_num(my_variable):
    numbers = re.findall(r'\d+', my_variable)
    return numbers[0]
def to_excel(data, existing_file='content.xlsx'):
    # 读取现有Excel文件以找到第一个空列
    # data是字典
    # 创建一个ExcelWriter对象

    # with pd.ExcelWriter('your_file.xlsx') as writer:
    #
    #     # 将data1写入第1行
    #     df1 = pd.DataFrame([data[0]])
    #     df1.to_excel(writer, index=False, startrow=0)
    #
    #     for i in data:
    #         if i >= 1:
    #             df2 = pd.DataFrame([data[i]])
    #             df2.to_excel(writer, header=False, index=False, startrow=i)
    try:
        existing_df = pd.read_excel(existing_file)
        start_col = len(existing_df.columns)
    except FileNotFoundError:
        start_col = 0  # 如果文件不存在，从第0列开始
    print(start_col)
    with pd.ExcelWriter(existing_file, engine='openpyxl', mode='a',if_sheet_exists='overlay') as writer:
        # 如果是从第0列开始，则写入头部
        if start_col == 0:
            df1 = pd.DataFrame([data[0]])
            df1.to_excel(writer, index=False, startrow=1, startcol=start_col)

        # 将其余数据写入
        for i in (data):
            if i >= 1:
                df = pd.DataFrame([data[i]])
                df.to_excel(writer, header=False, index=False, startrow=i+1, startcol=start_col)
def read_dict():





    sum_dict={}
    file_path = 'excel_result.txt'
    current_paragraph_number=None
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for line in lines:
        if "______________________"in line:
            line=line.strip()
            current_paragraph_number=to_num(line)
        elif "{" in line:
            line = line.strip()
            sum_dict[int(current_paragraph_number)]=ast.literal_eval(line)
            current_paragraph_number=None
    # print((sum_dict))
    to_excel(sum_dict)


read_dict()