# from selenium_chatgpt import selenium_spider
import json,re
from nltk.stem import WordNetLemmatizer
import random
import nltk
from nltk.corpus import stopwords
import pandas as pd
import openpyxl

def extract_element(data):
    print(data)

    # Extract the relevant string from the data
    try:
        labels_string = data["result_labels"]

        # Extract the portion that contains the JSON representation
        start_index = labels_string.index("{")
        end_index = labels_string.rindex("}") + 1
        json_str = labels_string[start_index:end_index]

        # Convert the string into a dictionary
        json_data = json.loads(json_str)
        labels_list = json_data["Labels_list"]
    except:
        result_labels_str = data['result_labels'].replace("'", "\"")
        result_labels_dict = json.loads(result_labels_str)

        # 提取 'Labels_list'
        labels_list = result_labels_dict['Labels_list']

    # Extract the list

    stop_words = set(stopwords.words('english'))

    # 去除停用词

    # 使用列表推导式分割含有空格的元素并组合成一个大列表
    split_and_combined_list = [word.split() if ' ' in word else [word] for word in labels_list]
    lemmatizer = WordNetLemmatizer()
    # 将嵌套的列表展平
    flattened_list = [item for sublist in split_and_combined_list for item in sublist]
    filtered_words = [word[:-1] if word.endswith("s") else lemmatizer.lemmatize(word) for word in flattened_list if word.lower() not in stop_words]
    abandon_list=['school','university','education','teacher','student','military','issue']
    text_data = [item for item in filtered_words if item.lower() not in abandon_list]
    text_data = ['US' if item == 'U.S.' else item for item in text_data]
    return (text_data)


def label_generate():
    xlsx_path=r'C:\Users\Morning\Desktop\hiwi\heart\paper\education.xlsx'
    df = pd.read_excel(xlsx_path)
    wb = openpyxl.load_workbook(xlsx_path)
    description_list = df["Overview"].fillna("", inplace=True)

    detailed_description_list = df["Content"]
    print(detailed_description_list)
    selenium_spider("",False,True)
    selenium_spider("I will give you a piece of news about education, I want you to give me relevant labels of it, each label should not exceed two words, please give me as much labels as possible, and in json format:{'Labels_list':[]}")
    for num, element in enumerate(detailed_description_list):
        if num==13:
            case_str = element[:10000]
            if num==0:
                result=selenium_spider(case_str,True,False,"4")
            else:
                result = selenium_spider(case_str, False, False,"4")
            result_dict={"num":num,"result_labels":result}
            with open("output_labels.jsonl", "a", encoding='utf-8') as f:

                f.write(json.dumps(result_dict) + "\n")
def cloud_chart(text_data_list):
    from wordcloud import WordCloud
    from collections import Counter
    from matplotlib.colors import LinearSegmentedColormap, rgb2hex
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt
    import matplotlib.pyplot as plt
    import json,jsonlines
    from matplotlib.colors import LinearSegmentedColormap
    from nltk.stem import WordNetLemmatizer
    # import gensim
    import itertools
    from scipy.spatial.distance import cosine
    abandon_list=['school','university','education','teacher','student']
    text_data = [item for item in text_data_list if item.lower() not in abandon_list]
    # 你的文本数据列表
    # text_data = [
    #     "apple", "banana", "cherry", "apple", "cherry", "date", "banana", "date", "date"
    # ]

    # 将文本数据列表转换为一个字符串，以便生成词云
    text = " ".join(text_data)
    word_counts = Counter(text_data)
    # 创建词云对象
    cmap = LinearSegmentedColormap.from_list("custom_cmap", ['#87CEFA', "#00008B"])

    # 创建一个基于频率的颜色函数
    def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
        relative_frequency = word_counts[word] / max(word_counts.values())
        rgba_color = cmap(relative_frequency)
        return rgb2hex(rgba_color)

    # 创建词云对象
    wordcloud = WordCloud(background_color="white",max_words=600, width=2000, height=800, color_func=color_func).generate_from_frequencies(word_counts)
    # wordcloud = WordCloud(background_color='white', max_words=600, width=2000, height=800).generate(text)
    plt.figure(figsize=(20, 10))  # 图像大小以英寸为单位

    # 可视化词云
    # plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
def bar_chart(text_data):
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt
    from collections import Counter

    # 你的文本数据列表
    # text_data = [
    #     "apple", "banana", "cherry", "apple", "cherry", "date", "banana", "date", "date"
    # ]

    # 将文本数据列表转换为一个字符串，以便生成词云
    text = " ".join(text_data)

    # 创建词云对象
    # wordcloud = WordCloud(width=800, height=800, background_color='white').generate(text)

    # 获取词频信息
    word_freq = Counter(text_data)

    # 获取前N个最频繁出现的词
    top_N = 30  # 你可以根据需要更改这个值
    top_words = word_freq.most_common(top_N)

    # 分离词和词频
    words, frequencies = zip(*top_words)

    # 创建条形图
    plt.figure(figsize=(10, 5))
    plt.barh(words, frequencies)
    plt.xlabel('Frequency')
    plt.ylabel('Words')
    plt.title('Top 30 Words Frequency')
    plt.gca().invert_yaxis()  # 翻转y轴，使最常见的词在上方显示
    plt.show()
def extract_dict():

    jsonl_file_path = 'output_labels.jsonl'  # 替换为你的文件路径

    # 用于存储解析后的JSON数据的列表
    json_data = []
    i=0
    with open(jsonl_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                i+=1


                data = json.loads(line)
                json_data.extend(extract_element(data))
                result_dict={"num":i,"word_list":extract_element(data)}
                # with open("output_labels_list.jsonl", "a", encoding='utf-8') as f:
                #
                #     f.write(json.dumps(result_dict) + "\n")
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                continue
    cloud_chart(json_data)
# word_cloud(    text_data = [
#         "apple", "banana", "cherry", "apple", "cherry", "date", "banana", "date", "date"
#     ])
extract_dict()