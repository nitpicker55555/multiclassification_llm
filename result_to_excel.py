import re,os
import pandas as pd

# def check_number(path):
#     # check if number is 99
#     file_path = path
#
#     with open(file_path, 'r', encoding="utf-8") as file:
#         content = file.read()
#
#     # Define the pattern to search for the last occurrence of "____...____" and the number to its left
#     pattern = re.compile(r'(\d+)_{2,}')
#
#     # Find all occurrences of the pattern in the content
#     matches = pattern.findall(content)
#
#     # Get the last matched number if any matches were found
#     last_number = (matches[-1]) if matches else None
#     return last_number

def each_file(filename):
    # last_number=int(check_number(filename))
    with open(filename,'r',encoding='utf-8') as file:
        text=file.read()
    relevant_judge= {}
    pattern = r'(\d+)__________________________________________________\n(.*?)(?=\n\d+__________________________________________________|\Z)'
    matches = re.findall(pattern, text, re.DOTALL)

    paragraphs = {}
    for match in matches:
        paragraph_number = int(match[0])
        paragraph_content = match[1].strip()
        paragraphs[paragraph_number] = paragraph_content
        if '"Is_relevant": true' in paragraph_content:
            relevant_judge[paragraph_number]=True
        else:
            relevant_judge[paragraph_number]=False
    return paragraphs,relevant_judge
def add_2_excel(filepath,filename,list_):
    print(filepath,filename)
    filename=filename.replace("case_text_","")
    filename=filename.replace(".txt",".xlsx")
    filepath_xlsx=r'C:\Users\Morning\Desktop\hiwi\case_spider\case\content_'
    try:
        df = pd.read_excel(filepath_xlsx+filename)
    except:
        filepath_xlsx=r'C:\Users\Morning\Desktop\hiwi\case_spider\content_'
        df = pd.read_excel(filepath_xlsx+filename)

    # 将新列数据转换为Series对象
    description_column1 = df['num']
    if len(list_[0]) < len(description_column1):
            list_[0].insert(0,False)
            list_[1].insert(0,'null')
    relevant_column = pd.Series(list_[0])

    overview_column=pd.Series(list_[1])

    # 将新列插入到第一个空白列
    df.insert(4, 'Relevant', relevant_column)
    df.insert(5, 'Overview', overview_column)
    filename=filename.replace(".xlsx","")
    # 保存到原來的文件夾

    df.to_excel(filepath+"\\"+"updated_file_"+filename+'.xlsx', index=False)
def read_folder_list():
    for folder in os.listdir(os.getcwd()):
        if folder.startswith('content_') and os.path.isdir(folder):

            folder_path = os.path.join(os.getcwd(), folder)
            count = 0
            num_cases = 0
            # 遍历文件夹中的每个txt文件
            for filename in os.listdir(folder_path):
                if filename.startswith("case_text_"):

                        print(folder_path+'\\'+filename)
                        relevant_content,relevant_judge=each_file(folder_path+'\\'+filename)
                        print(relevant_judge)
                        add_col=[list(relevant_judge.values()),list(relevant_content.values())]
                        add_2_excel(folder_path,filename,add_col)
read_folder_list()
# C:\Users\Morning\Desktop\hiwi\case_spider\case\content_autonomous_driving_accidents.xlsx