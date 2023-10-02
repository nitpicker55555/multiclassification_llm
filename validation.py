import os

import pandas as pd
import json
# Load the Excel file into a DataFrame
file_path = 'semantic_combine.csv'
# file_path='Geo-AI ethics cases.xlsx'
df = pd.read_csv(file_path)
from itertools import islice
def csv_to_json(num):
    cate="Risk to Human Rights	instances with privacy violations	privacy sensitivity	privacy violations severity	instances with injustice to rights	Severity of injustice	instances involving vulnerable groups	emotional and psychological harm	vulnerable groups affected	cases where harm is reversible	affected by challenges to self-identity and values	Severity of emotional and psychological harm	instances where the harm persists	Physical harm	Severity of Physical harm 	instances where the physical harm persists	cases where the physical harm is reversible	instances where the harm is easily detectable	Economic loss	instances where economic losses persist	the severity of economic impact	extent of impact is fixed	affected individuals	affected local population	global implications	Whether humans can be replaced	Whether there is a law to regulate	AI-based specificity	cases affected by untimely data training and maintenance	cases affected by opaque and recurring weak capacities	cases affected due to limitations of traditional supervisory methods	lifecycle time period-planning and design	lifecycle time period-collection and processing data	lifecycle time period-building usage model	lifecycle time period-verification and verification	lifecycle time period-deployment 	lifecycle time period-Operation and Monitoring	lifecycle time period-End User Use and Impact	Geographical Attributes-Timeliness	Geographical Attributes-Accuracy	Data Production Process -Acquisition	Data Production Process-Preprocessing	Data Production Process-Integration	Data Production Process-Storage and Management	Data Production Process-Analysis and Processing	Data Production Process-Application Communication"
    cate='"'+cate.replace("\t",'","')+'"'
    labels_=cate.split("\t")
    # print(cate)

    sum_dict_={}

    system_dict={'role':'system','content':'Given a news text, provide the following fields in a JSON dict, where applicable:'+str(cate)}
    user_dict={'role':'user','content':''}
    assistant_dict={'role':'assistant','content':''}
    # print(system_dict)


#df.shape[0]
    sum_csv=[]
    first_key_values=[]
    for i in range(df.shape[0]):
        short_str=df['Description'][i]
        long_str=df['Detailed Description'][i]
        if pd.isna(long_str):
            long_str=""
        user_dict['content']=short_str+long_str

        # print('{"messages": [{"role": "system", "content": "Given a news text, provide the following fields in a JSON dict, where applicable:')
        subset_df = df.loc[i, 'Risk to Human Rights':].to_dict()
        assistant_dict['content'] = str(subset_df)
        sum_dict_['messages']=[system_dict,user_dict,assistant_dict]
        # with open('data.jsonl', 'a') as json_file:
        #     json.dump(sum_dict_, json_file)
        #     json_file.write('\n')  # 在每个字典后面添加换行符
        sum_csv.append(subset_df)
        # print(subset_df)
    for dict_str in sum_csv:
        # Convert the string to a Python dictionary
        dict_obj = dict_str

        # Get the first key-value pair
        first_key, first_value =  next(iter(islice(dict_obj.items(),num,num+1)))

        # Append the first key-value pair to the list
        first_key_values.append({first_key: first_value})
    # print(first_key_values)
    return first_key_values
        # print(df['Description'][0],df['Detailed Description'][0])

def read_result(num,file_path):
    import ast

    # file_path = 'result_tem_1p2_top_0_73.txt'

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    import re

    # Regular expression to find the dictionary-like structures in the content
    pattern = r"\{[^}]*\}"

    # Search for all the matches
    matches = re.findall(pattern, content)

    # Display the first matched dictionary if any are found
    first_dict_str = matches[1] if matches else "No dictionary found"
    # print(matches)

    first_key_values = []

    # Loop through each dictionary string in the matches list
    for dict_str in matches:
        # Convert the string to a Python dictionary
        try:
            dict_obj = ast.literal_eval(dict_str)
        except:
            print("___________________________________")
            print(dict_str)
            print("___________________________________")
        # Get the first key-value pair  截取字典的每个键，然后可以为每个键都计算accuracy
        #next(islice(dict_iterator, 1, 2))
        first_key, first_value = next(iter(islice(dict_obj.items(),num,num+1)))

        # Append the first key-value pair to the list
        first_key_values.append({first_key: first_value})
    # print(first_key_values)
    return first_key_values
def calculation():
    # import pandas as pd

    # 读取CSV文件
    # df = pd.read_csv('your_file.csv')

    # 创建一个字典用于存储每一列的唯一数据类型
    column_types = {}

    cols_with_two_unique_values = []

    # 遍历所有列
    for col in df.columns:
        # 如果该列的唯一值数超过2
        if len(df[col].dropna().unique()) == 2:
            cols_with_two_unique_values.append(col)

    # 输出结果
    print(cols_with_two_unique_values)
    return cols_with_two_unique_values
def score():
    import sys
    folder_path = '.'
    binary_list=['Risk to Human Rights', 'instances with privacy violations', 'instances with injustice to rights', 'instances involving vulnerable groups', 'emotional and psychological harm', 'vulnerable groups affected', 'cases where harm is reversible', 'affected by challenges to self-identity and values', 'instances where the harm persists', 'Physical harm', 'instances where the physical harm persists', 'cases where the physical harm is reversible', 'instances where the harm is easily detectable', 'Economic loss', 'instances where economic losses persist', 'extent of impact is fixed', 'affected individuals', 'affected local population', 'global implications', 'Whether humans can be replaced', 'Whether there is a law to regulate', 'AI-based specificity', 'cases affected by untimely data training and maintenance', 'cases affected by opaque and recurring weak capacities', 'cases affected due to limitations of traditional supervisory methods', 'lifecycle time period-planning and design', 'lifecycle time period-collection and processing data', 'lifecycle time period-building usage model', 'lifecycle time period-verification and verification', 'lifecycle time period-deployment ', 'lifecycle time period-Operation and Monitoring', 'lifecycle time period-End User Use and Impact', 'Geographical Attributes-Timeliness', 'Geographical Attributes-Accuracy', 'Data Production Process -Acquisition', 'Data Production Process-Preprocessing', 'Data Production Process-Integration', 'Data Production Process-Storage and Management', 'Data Production Process-Analysis and Processing', 'Data Production Process-Application Communication']
    subset_df = df.loc[:, 'Risk to Human Rights':].to_dict()
    original_stdout = sys.stdout

    # 打开一个文件以写入
    with open('output_log.txt', 'w') as fileread:
        sys.stdout = fileread  # 将 stdout 重定向到文件
        for filename in os.listdir(folder_path):
            # 检查文件名是否以'result'开头
            if filename.startswith('result'):



            # print(subset_df.keys())
                print("++++++++++++++++++++++++++")
                print(filename,"not binary labels score:")
                result_point=[]
                for i in range(len(subset_df)):
                    if list(subset_df.keys())[i] not in binary_list:
                        sample_list = csv_to_json(i)
                        first_key_values = read_result(i,filename)
                        identical_count = sum(a == b for a, b in zip(first_key_values, sample_list))
                        percentage_identical = (identical_count / len(first_key_values)) * 100
                        result_point.append(percentage_identical)
                        print(list(subset_df.keys())[i],identical_count,percentage_identical)

                print('\n')
                # print(filename)
                # print('\n')
                print(filename,"not binary score average",sum(result_point)/(len(subset_df)-len(binary_list)))
                print('\n')

                print(filename, "binary labels score:")

                for i in range(len(subset_df)):
                    if list(subset_df.keys())[i] in binary_list:
                        sample_list = csv_to_json(i)
                        first_key_values = read_result(i, filename)
                        identical_count = sum(a == b for a, b in zip(first_key_values, sample_list))
                        percentage_identical = (identical_count / len(first_key_values)) * 100
                        result_point.append(percentage_identical)
                        print(list(subset_df.keys())[i],"score:",  percentage_identical)

                print('\n')
                # print(filename)
                # print('\n')
                print(filename,"binary score average",sum(result_point) / (len(binary_list)))
                print('\n')
def draw_pic():
    import re,sys
    labels = []
    for filename in os.listdir('.'):
        # 检查文件名是否以'result'开头
        if filename.startswith('result'):
            labels.append(filename.strip(".txt"))
    file_path = 'output_log.txt'

    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.readlines()
    # Update the regular expressions to only match ".txt binary score average" and ".txt not binary score average"
    binary_score_pattern = re.compile(r"\.txt binary score average (\d+\.?\d*)")
    not_binary_score_pattern = re.compile(r"\.txt not binary score average (\d+\.?\d*)")

    # Initialize lists to store the binary and not binary scores
    binary_scores = []
    not_binary_scores = []

    # Parse the file content again
    for line in file_content:
        binary_score_match = binary_score_pattern.search(line)
        not_binary_score_match = not_binary_score_pattern.search(line)

        if binary_score_match:
            binary_scores.append(float(binary_score_match.group(1)))

        if not_binary_score_match:
            not_binary_scores.append(float(not_binary_score_match.group(1)))

    # Show the extracted data for verification
    import matplotlib.pyplot as plt
    import numpy as np

    # Define the labels and data
    # labels = [f"result_{i}.txt" for i in range(len(binary_scores))]
    binary_data = binary_scores
    not_binary_data = not_binary_scores

    # Define the positions and width for the bars
    x = np.arange(len(labels))
    width = 0.35

    # Create the bar chart
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, binary_data, width, label='Binary Score Average')
    rects2 = ax.bar(x + width/2, not_binary_data, width, label='Not Binary Score Average')

    # Add labels, title and legend
    ax.set_ylabel('Scores')
    ax.set_title('Average Scores of Model')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    # Annotate the bars with their values
    for rect in rects1 + rects2:
        height = rect.get_height()
        ax.annotate(f"{height:.2f}",
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

    # Show the plot
    plt.show()



# score()
draw_pic()
