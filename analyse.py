import os,json

# 获取当前工作目录
current_dir = os.getcwd()

# 初始化一个字典来存储每个文件夹中'Is_relevant=True'的数量
folder_count = {}

# 遍历当前目录下的每个以"content"开头的文件夹
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
                        file_num+=content.count('Is_relevant": false')

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
                    attribute_dict[key + "_" + value] = round(count / sum(values.values()), 2)
                    print(f"    Value: {value}, Count: {count}")

            if (true_num, false_value) != (0, 0):

                num_value_list.append((true_num / (true_num + false_value)) * 100)
                attribute_dict[key] = round(true_num / (true_num + false_value), 2)
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
                if filename.endswith('classification_result_json.jsonl'):
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
                    attribute_dict = iteration(filename.replace("classification_result_json.jsonl","").replace("updated_file_",""),query_attribute)
                    with open('attribute_num_json.jsonl', 'a') as json_file:
                        json_str = json.dumps(attribute_dict)
                        json_file.write(json_str + '\n')


            print(dirpath,"dirpath===")

            content_folder_list.append(dirpath[2:])
            attribute_dict=iteration( "SUM_" + dirpath[2:],counter)

            with open('attribute_num_json.jsonl', 'a') as json_file:
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

    content_folder_list=(content_folder_list+attribute_list)
    print(len(content_folder_list))
    print(content_folder_list)
    # draw_plotify(content_folder_list,4,num_value_list)
# normal_analyse()
# get_number("autonomous_driving_accidents")
def generate_excel():
    import json

    # Read the jsonl file
    with open("attribute_num_json.jsonl", "r") as file:
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
    output_path = "attribute_num_json.xlsx"
    df.to_excel(output_path, index=False)
# generate_excel()
# with open('attribute_num_json.jsonl', 'w') as file:
#     pass
# annotion_analyse()
normal_analyse()
# clean_json()