import os
import json
from datetime import datetime
import plotly.io as pio
def count_positive_in_jsonl(folder_path):
    topic_list={}

    # 遍历指定文件夹中的所有文件
    for filename in os.listdir(folder_path):
        if "2" in filename:
            if filename.split("20")[0] not in topic_list and "merged" not in filename:
                topic_list[filename.split("20")[0]]=[]
            if "merged" not in filename:
                topic_list[filename.split("20")[0]].append(filename)
    for topic in topic_list:
        print(topic)
        sum_counts={}
        positive_counts = {}
        negative_counts = {}
        neutral_counts = {}
        time_dict = {}
        for filename in topic_list[topic]:
            # 检查文件名是否以 "sentiment" 结尾并且是 `.jsonl` 格式
            if filename.endswith("_profile.jsonl"):
                file_path = os.path.join(folder_path, filename)
                # 打开并读取文件中的每一行
                time_dict[filename.split("_without")[0]]={}
                with open(file_path, 'r', encoding='utf-8') as file:
                    for num,line in enumerate(file):
                            # 解析 JSON
                            data = json.loads(line)
                            time_dict[filename.split("_without")[0]][num]=data['time'].split("T")[0]
        for filename in topic_list[topic]:
            if filename.endswith("complete.jsonl"):
                file_path = os.path.join(folder_path, filename)
                positive_count = 0
                negative_count=0
                # 打开并读取文件中的每一行
                with open(file_path, 'r', encoding='utf-8') as file:
                    for line in file:
                        try:
                            # 解析 JSON
                            data = json.loads(line)


                            try:
                                time_str=time_dict[filename.split("_without")[0]][data['num']]
                                if time_str not in sum_counts:
                                    sum_counts[time_str]=0
                                    positive_counts[time_str]=0
                                    negative_counts[time_str]=0
                                    neutral_counts[time_str]=0

                                # 检查并计数 "positive" 键
                                sum_counts[time_str]+=1
                                if 'positive' in data['sentiment']:
                                    positive_counts[time_str] += 1
                                elif 'negative' in data['sentiment']:
                                    negative_counts[time_str] += 1
                                elif 'neutral' in data['sentiment']:
                                    neutral_counts[time_str] += 1
                            except KeyError:
                                print(filename.split("_without")[0],[data['num']])
                        except json.JSONDecodeError:
                            # 如果有行不是有效的 JSON，则忽略
                            pass

                # 将结果保存到字典中
                # positive_counts[filename.split("_without")[0]] = positive_count/(positive_count+negative_count)
                # negative_counts[filename] = negative_count
        print(positive_counts)
        print(negative_counts)
        plot_multiple_line_charts({"sum_counts":sum_counts,"positive_counts":positive_counts,"negative_counts":negative_counts,"neutral_counts":neutral_counts},topic)
    # return positive_counts
import plotly.graph_objs as go

def plot_multiple_line_charts(data_dict,topic):
    fig = go.Figure()

    for name, data in data_dict.items():
        # 将键转换为日期并排序
        sorted_items = sorted(data.items(), key=lambda x: datetime.strptime(x[0], '%Y-%m-%d'))

        # 分离排序后的日期和数值
        x_values = [item[0] for item in sorted_items]
        y_values = [item[1] for item in sorted_items]

        # 向图表中添加折线
        fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='lines+markers', name=name,line=dict(width=2)))

    # 添加标题和轴标签
    fig.update_layout(title='Line chart of emotions over time',
                      xaxis_title='date',
                      yaxis_title='value')

    # 显示图表
    # fig.show()
    pio.write_html(fig, file='tem_file\\emotion_%s.html' % topic)


folder_path = r'C:\Users\Morning\Desktop\hiwi\heart\paper\hi_structure\twitter_data2'

count_positive_in_jsonl(folder_path)