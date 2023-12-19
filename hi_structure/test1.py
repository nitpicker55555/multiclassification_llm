
import openai
import numpy as np
import pandas as pd
import numpy as np
import os
from scipy.spatial import distance
# 设置您的 OpenAI API 密钥
openai.api_key = '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'

def generate():
    def text_to_vector(text):
        response = openai.Embedding.create(
            input=text,
            engine="text-embedding-ada-002"
        )


        # 保存为CSV文件
        np.save(text+"ttt.npy", response['data'][0]['embedding'])
        return response['data'][0]['embedding']
    word=["garden city",
    "pre-industrial",
    "residential",
    "commercial"]
    for i in word:
      text_to_vector(i)
def read_emb():
    label_list=[]
    emb_List=[]
    for dirpath, dirnames, filenames in os.walk(r"C:\Users\Morning\Desktop\hiwi\heart\paper\hi_structure"):
        # Check if the directory starts with "content"
        for filename in filenames:
            if filename.endswith("ttt.npy"):
                print(dirpath,filename)
                emb_List.append(np.load(dirpath+"\\"+filename))
                label_list.append(filename.replace("ttt.npy",""))
    print(calculate_distances_with_labels(emb_List, label_list))
def calculate_distances_with_labels(embeddings, labels):
    """
    计算嵌入之间的距离并与标签相关联。

    参数：
    embeddings (list of numpy.ndarray): 包含嵌入的列表，每个元素是一个嵌入向量的NumPy数组。
    labels (list): 包含与每个嵌入向量对应的标签的列表。

    返回：
    distances_with_labels (list of tuple): 每个元素是一个元组 (label_i, label_j, dist)，
    表示标签label_i和标签label_j对应的嵌入之间的距离dist，按距离升序排列。
    """
    num_embeddings = len(embeddings)
    distances_with_labels = []

    # 计算所有嵌入之间的距离并与标签相关联
    for i in range(num_embeddings):
        for j in range(i + 1, num_embeddings):
            dist = distance.euclidean(embeddings[i], embeddings[j])
            label_i = labels[i]
            label_j = labels[j]
            distances_with_labels.append((label_i, label_j, dist))

    # 按距离升序排序
    sorted_distances_with_labels = sorted(distances_with_labels, key=lambda x: x[2])

    return sorted_distances_with_labels
# generate()
read_emb()