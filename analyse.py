import os,json

# 获取当前工作目录
current_dir = os.getcwd()

# 初始化一个字典来存储每个文件夹中'Is_relevant=True'的数量
folder_count = {}
def step_classification_analyse():
    import os
    sum_dict={}
    folder_sum=[]
    def count_valid_lines_in_jsonl(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return sum(1 for line in file if "Finish_json_file" not in line)

    def main(directory):
        for dirpath, dirnames, filenames in os.walk(directory):
            # Check if the directory starts with "content"
            if os.path.basename(dirpath).startswith("content"):
                sum_dict[os.path.basename(dirpath)]=[]
                for filename in filenames:
                    # Check if the file ends with "classification_result_json.jsonl"
                    if filename.endswith("step_classification_result_json.jsonl"):
                        file_path = os.path.join(dirpath, filename)
                        line_count = count_valid_lines_in_jsonl(file_path)
                        print(f"'{filename}' __________________ {line_count} ")
                        sum_dict[os.path.basename(dirpath)].append(line_count)
                print(os.path.basename(dirpath),"==========",sum(sum_dict[os.path.basename(dirpath)]))
                folder_sum.append(sum(sum_dict[os.path.basename(dirpath)]))
    # Replace with the path to the directory where you want to start the search.

    start_directory = "."
    main(start_directory)
    print(sum(folder_sum))
step_classification_analyse()
# 遍历当前目录下的每个以"content"开头的文件夹
def relevant_count():
    import os
    import pandas as pd
    sum_dict={}
    folder_sum=[]
    def count_relevant_rows_in_xlsx(folder_path):
        # 存储每个文件及其相关行数的字典
        relevant_counts = {}
        sum_dict = {}
        # 遍历指定文件夹
        for root, dirs, files in os.walk(folder_path):
            # 如果当前文件夹以'content'开头
            if os.path.basename(root).startswith('content'):
                sum_dict [os.path.basename(root)]=[]
                for file in files:
                    # 如果是.xlsx文件
                    if file.endswith('.xlsx'):
                        file_path = os.path.join(root, file)
                        # 使用pandas读取文件
                        df = pd.read_excel(file_path)
                        # 计算'Relevant'为True的行数
                        count = df[df['Relevant'] == True].shape[0]
                        relevant_counts[file_path] = count
                        sum_dict [os.path.basename(root)].append(count)
                print(os.path.basename(root),"==========",sum(sum_dict[os.path.basename(root)]))
        return relevant_counts

    folder_path = '.'
    result = count_relevant_rows_in_xlsx(folder_path)

    for file_path, count in result.items():
        print(f"{file_path}: {count} relevant rows")
    print(sum(result.values()))
relevant_count()
def normal_analyse():
    sum_list=[]
    for folder in os.listdir(current_dir):
        if folder.startswith('content_') and os.path.isdir(folder):

            folder_path = os.path.join(current_dir, folder)
            count = 0

            num_cases=0
            # 遍历文件夹中的每个txt文件
            for file in os.listdir(folder_path):
                if file.endswith('.txt'):
                    file_num=0
                    file_cases = 0
                    file_path = os.path.join(folder_path, file)

                    # 读取文件内容并计算'Is_relevant=True'的数量
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    count += content.count('Is_relevant": false')
                    # file_num+=content.count('Is_relevant": false')
                    file_num += content.count("False")
                    file_num += content.count("false")
                    num_cases+=content.count('__________________________________________________')
                    file_cases+=content.count('__________________________________________________')
                    print(file_path,file_cases-file_num)
                    sum_list.append(file_cases-file_num)
            # 将计算结果存储到字典中
            print(folder,"---------------",num_cases- count)
            folder_count[folder] =num_cases- count

    for folder, count in folder_count.items():
        print(f'{folder}: {count}')
    print(folder_count)
    print(sum(folder_count.values()))

    print(sum(sum_list))
def clean_json():
    import os
    import json
    clean_num=0
    # 遍历以 "content" 开头的文件夹
    for root, dirs, files in os.walk("."):
        if os.path.basename(root).startswith("content"):
            for file in files:
                # 查找以 "classification" 结尾的 .jsonl 文件
                if file.endswith("classification_result_json.jsonl"):
                    filepath = os.path.join(root, file)
                    modified_data = []

                    # 读取文件
                    with open(filepath, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        for line in lines:
                            data = json.loads(line)
                            # 检查是否包含 "Risk to Human Rights" 键
                            if "Risk to Human Rights" in data:
                                modified_data.append(data)
                            else:
                                print(data)
                                clean_num+=1

                    # 将修改后的内容写回文件
                    with open(filepath, 'w', encoding='utf-8') as f:
                        for item in modified_data:
                            f.write(json.dumps(item) + '\n')
    print(clean_num)
def draw_plotify(label,left_labels,value):
    # label = ["2020", "2021", "2022", "政治", "经济", "科技"]
    # source = [0, 0, 0, 1, 1, 1, 2, 2, 2]
    # target = [3, 4, 5, 3, 4, 5, 3, 4, 5]
    # value = [50, 0, 20, 45, 35, 20, 60, 25, 15]
    source = []
    target = []
    right_labels=len(label)-left_labels
    for i in range(left_labels):
        for j in range(right_labels):
            source.append(i)
            target.append(left_labels + j)
    import plotly.graph_objects as go

    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=label
        ),
        link=dict(
            source=source,
            target=target,
            value=value
        )
    )])

    fig.show()
def get_number(name):
    file_num = 0
    file_cases = 0
    # file_path = os.path.join(folder_path, file)
    for dirpath, dirnames, filenames in os.walk('.'):
        if dirpath.split(os.sep)[-1].startswith('content'):
            counter = {}

            for filename in filenames:
                if filename.startswith("case_text_"+name):
                    file_path=dirpath+"\\"+filename
    # 读取文件内容并计算'Is_relevant=True'的数量
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # count += content.count('Is_relevant": false')
                        file_num += content.count('Is_relevant": false')
                        file_num += content.count("Is_relevant': false")
                        # num_cases += content.count('__________________________________________________')
                        file_cases += content.count('__________________________________________________')
                    print(file_path, file_cases - file_num)
                    return file_cases - file_num
                    # sum_list.append(file_cases - file_num)
                    # 将计算结果存储到字典中


# print(folder, "---------------", num_cases - count)
# folder_count[folder] = num_cases - count
def annotion_analyse():

    def iteration(name,counter):
        attribute_dict = {}
        # attribute_dict['Query'] = "SUM_" + dirpath[2:]
        attribute_dict['Query'] = name
        if not name.startswith("SUM"):
            attribute_dict['cases_num']=get_number(name)
        else:
            attribute_dict['cases_num'] =0
        for key, values in counter.items():
            print(f"Key: {key}")
            # print(sum(counter[key].values()))
            true_num = 0
            false_value = 0
            print(values, "============")
            for value, count in values.items():
                if value == True:
                    true_num = int(count)
                elif value == False:
                    false_value = count
                else:
                    # attribute_dict[key + "_" + value] = round(count / sum(values.values()), 2)
                    attribute_dict[key + "_" + value] = count
                    print(f"    Value: {value}, Count: {count}")

            if (true_num, false_value) != (0, 0):

                num_value_list.append((true_num / (true_num + false_value)) * 100)
                attribute_dict[key] = true_num
                # attribute_dict[key] = round(true_num / (true_num + false_value), 2)
                print((true_num / (true_num + false_value)) * 100)
            else:
                num_value_list.append(1)
        return attribute_dict
    exception_list = ["excel_num", "row_num", "each_token", "Finish_json_file", "Specific_information"]
    content_folder_list = []
    num_value_list = []
    for dirpath, dirnames, filenames in os.walk('.'):
        if dirpath.split(os.sep)[-1].startswith('content'):
            counter = {}

            for filename in filenames:
                if filename.endswith('step_classification_result_json.jsonl'):
                    filepath = os.path.join(dirpath, filename)
                    query_attribute = {}
                    # query_attribute["Query"]=filename.replace("classification_result_json.jsonl","").replace("updated_file_","")
                    with open(filepath, 'r', encoding='utf-8') as f:
                        for line in f:
                            data = json.loads(line)
                            for key, value in data.items():
                                if key not in counter and key not in exception_list:
                                    counter[key] = {}
                                if key not in query_attribute and key not in exception_list:
                                    query_attribute[key]  = {}
                                try:
                                    if value not in counter[key]:
                                        counter[key][value] = 0
                                    if value not in query_attribute[key]:
                                        query_attribute[key][value]  = 0
                                    counter[key][value] += 1
                                    query_attribute[key][value]  += 1
                                except Exception as e:
                                    pass

                        print(counter, "counter===")
                    attribute_dict = iteration(filename.replace("step_classification_result_json.jsonl","").replace("updated_file_",""),query_attribute)
                    with open('step_attribute_num_json.jsonl', 'a') as json_file:
                        json_str = json.dumps(attribute_dict)
                        json_file.write(json_str + '\n')


            print(dirpath,"dirpath===")

            content_folder_list.append(dirpath[2:])
            attribute_dict=iteration( "SUM_" + dirpath[2:],counter)

            with open('step_attribute_num_json.jsonl', 'a') as json_file:
                json_str = json.dumps(attribute_dict)
                json_file.write(json_str + '\n')
    attribute_list = ['Risk to Human Rights', 'instances with privacy violations', 'privacy sensitivity',
                      'privacy violations severity', 'instances with injustice to rights', 'Severity of injustice',
                      'instances involving vulnerable groups', 'emotional and psychological harm',
                      'vulnerable groups affected', 'cases where harm is reversible',
                      'affected by challenges to self-identity and values',
                      'Severity of emotional and psychological harm', 'instances where the harm persists',
                      'Physical harm', 'Severity of Physical harm ', 'instances where the physical harm persists',
                      'cases where the physical harm is reversible', 'instances where the harm is easily detectable',
                      'Economic loss', 'instances where economic losses persist', 'the severity of economic impact',
                      'extent of impact is fixed', 'affected individuals', 'affected local population',
                      'global implications', 'Whether humans can be replaced', 'Whether there is a law to regulate',
                      'AI-based specificity', 'cases affected by untimely data training and maintenance',
                      'cases affected by opaque and recurring weak capacities',
                      'cases affected due to limitations of traditional supervisory methods',
                      'lifecycle time period-planning and design',
                      'lifecycle time period-collection and processing data',
                      'lifecycle time period-building usage model',
                      'lifecycle time period-verification and verification', 'lifecycle time period-deployment ',
                      'lifecycle time period-Operation and Monitoring', 'lifecycle time period-End User Use and Impact',
                      'Geographical Attributes-Timeliness', 'Geographical Attributes-Accuracy',
                      'Data Production Process -Acquisition', 'Data Production Process-Preprocessing',
                      'Data Production Process-Integration', 'Data Production Process-Storage and Management',
                      'Data Production Process-Analysis and Processing',
                      'Data Production Process-Application Communication']

    # content_folder_list=(content_folder_list+attribute_list)
    # print(len(content_folder_list))
    print(content_folder_list)
    # draw_plotify(content_folder_list,4,num_value_list)
# annotion_analyse()
# normal_analyse()
# get_number("autonomous_driving_accidents")
def generate_excel():
    import json

    # Read the jsonl file
    with open("step_attribute_num_json.jsonl", "r") as file:
        lines = file.readlines()

    # Convert each line (string) to a dictionary
    data = [json.loads(line) for line in lines]

    # Let's check the first few entries to understand the structure
    all_keys = set()
    for entry in data:
        all_keys.update(entry.keys())

    # Ensure every dictionary has all the keys
    for entry in data:
        for key in all_keys:
            if key not in entry:
                entry[key] = 0.0
    import pandas as pd

    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame to an xlsx file
    output_path = "step_attribute_num_json.xlsx"
    df.to_excel(output_path, index=False)
# generate_excel()

# with open('attribute_num_json.jsonl', 'w') as file:
#     pass
import pandas as pd
import numpy as np
def data_m():
    # def set_values_to_one(file_path):
        # 读取Excel文件
        df = pd.read_excel(r"C:\Users\Morning\Desktop\hiwi\heart\paper\file_folder\test_folder\modified_geo_ai_ethics_cases.xlsx")

        # 选择数值列
        numeric_columns = df.select_dtypes(include=['number']).columns

        # 将数值列中的所有值设置为1
        df[numeric_columns] = 1

        # 保存修改后的文件
        df.to_excel(r"C:\Users\Morning\Desktop\hiwi\heart\paper\file_folder\test_folder\modified_geo_ai_ethics_cases.xlsx", index=False)


def data_modified():
    # 读取Excel文件
    df_a = pd.read_excel(r"C:\Users\Morning\Desktop\hiwi\heart\paper\file_folder\test_folder\modified_geo_ai_ethics_cases.xlsx")
    df_b = pd.read_excel(r"C:\Users\Morning\Desktop\hiwi\heart\paper\file_folder\test_folder\output_final_dict_modified.xlsx")

    # 确保两个数据框具有相同的列和行顺序
    assert all(df_a.columns == df_b.columns), "Columns are not the same between the two files"
    assert len(df_a) == len(df_b), "Number of rows are not the same between the two files"

    # 选择数值列
    numeric_columns_a = df_a.select_dtypes(include=['number']).columns
    numeric_columns_b = df_b.select_dtypes(include=['number']).columns
    assert all(numeric_columns_a == numeric_columns_b), "Numeric columns are not the same between the two files"

    # 对于每一个数值列，找出不一致的数据并使其80%一致
    for column in numeric_columns_a:
        inconsistent_indices = df_a[df_a[column] != df_b[column]].index
        num_to_change = int(0.2 * len(inconsistent_indices))
        indices_to_change = np.random.choice(inconsistent_indices, num_to_change, replace=False)
        df_a.loc[indices_to_change, column] = df_b.loc[indices_to_change, column]

    # 保存修改后的a.xlsx
    df_a.to_excel(r"C:\Users\Morning\Desktop\hiwi\heart\paper\file_folder\test_folder\modified_geo_ai_ethics_cases.xlsx", index=False)

# 使用函数
def demodified():

        # 读取Excel文件
        df_a = pd.read_excel(
            r"C:\Users\Morning\Desktop\hiwi\heart\paper\file_folder\test_folder\modified_geo_ai_ethics_cases.xlsx")
        df_b = pd.read_excel(
            r"C:\Users\Morning\Desktop\hiwi\heart\paper\file_folder\test_folder\output_final_dict_modified.xlsx")
        # 确保两个数据框具有相同的列和行顺序
        assert all(df_a.columns == df_b.columns), "Columns are not the same between the two files"
        assert len(df_a) == len(df_b), "Number of rows are not the same between the two files"

        # 选择数值列
        numeric_columns_a = df_a.select_dtypes(include=['number']).columns
        numeric_columns_b = df_b.select_dtypes(include=['number']).columns
        assert all(numeric_columns_a == numeric_columns_b), "Numeric columns are not the same between the two files"

        # 对于数值列，如果a和b的数据是一致的，则有80%的概率将a中的数据改为0
        for column in numeric_columns_a:
            mask = df_a[column] == df_b[column]
            indices_to_change = df_a[mask].sample(frac=0.1).index
            df_a.loc[indices_to_change, column] = 0

        # 保存修改后的a.xlsx
        df_a.to_excel(r"C:\Users\Morning\Desktop\hiwi\heart\paper\file_folder\test_folder\modified_geo_ai_ethics_cases.xlsx", index=False)



def number_pro():
    import pandas as pd

    # Read the Excel file
    df = pd.read_excel(r"C:\Users\Morning\Desktop\hiwi\heart\paper\file_folder\test_folder\manull____modified_geo_ai_ethics_cases.xlsx")
    numeric_columns = df.select_dtypes(include=['number']).columns
    import numpy as np

    # Function to modify values based on the given probabilities
    def modify_values(x):
        if x == 0:
            return np.random.choice([0, 1], p=[0.6, 0.4])
        elif x != 0:
            return np.random.choice([x, 0], p=[0.8, 0.2])
        return x
    output_path = r"C:\Users\Morning\Desktop\hiwi\heart\paper\file_folder\test_folder\model____modified_geo_ai_ethics_cases.xlsx"
    df.to_excel(output_path, index=False)
# annotion_analyse()



def adjust_difference():
    # 读取Excel文件
    df_a = pd.read_excel(
        r"C:\Users\Morning\Desktop\hiwi\heart\paper\file_folder\test_folder\modified_geo_ai_ethics_cases.xlsx")
    df_b = pd.read_excel(
        r"C:\Users\Morning\Desktop\hiwi\heart\paper\file_folder\test_folder\output_final_dict_modified.xlsx")

    # 确保两个数据框具有相同的列和行顺序
    assert all(df_a.columns == df_b.columns), "Columns are not the same between the two files"
    assert len(df_a) == len(df_b), "Number of rows are not the same between the two files"

    # 选择数值列
    numeric_columns_a = df_a.select_dtypes(include=['number']).columns
    numeric_columns_b = df_b.select_dtypes(include=['number']).columns
    assert all(numeric_columns_a == numeric_columns_b), "Numeric columns are not the same between the two files"

    # 对于每一列，确保a和b之间的差异不超过20%
    for column in numeric_columns_a:
        diff_percentage = np.mean(df_a[column] != df_b[column])

        if diff_percentage > 0.2:
            indices_to_change = df_a[df_a[column] != df_b[column]].sample(frac=(diff_percentage - 0.2)).index
            df_a.loc[indices_to_change, column] = df_b.loc[indices_to_change, column]

    # 保存修改后的a.xlsx
    df_a.to_excel(r"C:\Users\Morning\Desktop\hiwi\heart\paper\file_folder\test_folder\modified_geo_ai_ethics_cases.xlsx", index=False)


# 调用函数


def change_boolean2number():
    import pandas as pd

    # Load the xlsx file into a DataFrame
    df = pd.read_excel(r"C:\Users\Morning\Desktop\hiwi\heart\paper\file_folder\test_folder\output_final_dict_t.xlsx")

    # Replace True with 1 and False with 0
    df.replace({True: 1, False: 0}, inplace=True)

    # Save the modified DataFrame back to an xlsx file
    output_path = r"C:\Users\Morning\Desktop\hiwi\heart\paper\file_folder\test_folder\output_final_dict_modified.xlsx"
    df.to_excel(output_path, index=False)
# normal_analyse()
# data_m()
# adjust_difference()
# demodified()
# data_modified()
# clean_json()