from collections import Counter
import json
from sklearn.cluster import DBSCAN
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA
import json,re
from sentence_transformers import SentenceTransformer
# Load the JSONL file
from scipy.spatial import distance
import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
def get_clean_word(file_path,top_words=None):
    # file_path = 'output_labels_list.jsonl'

    # Read and parse the JSONL file
    with open(file_path, 'r') as file:
        # Read the lines in the file
        lines = file.readlines()
        # Parse each line as a JSON object
        data = [json.loads(line) for line in lines]

    # Initialize a Counter object to hold the word frequencies
    # word_freq = Counter()


    # Initialize the WordNet lemmatizer
    # sum_set=set()
    sum_list=[]

    for entry in data:
        word_list = entry['label_list']
        # for word in word_list:
        #     sum_set.add(word)
        sum_list.extend(word_list)
        # Update the word frequencies
        # word_freq.update(word_list)
    print("original length:",len(sum_list))
    # print("original no repeat length:", len(sum_set))
    # all_word_list_before_clean_num = sum(1 for word, freq in word_freq.items() if freq == 1)
    # print(all_word_list_before_clean_num)


    # 初始化词形还原器
    lemmatizer = WordNetLemmatizer()



    # 确保已下载所需的 NLTK 资源
    nltk.download('wordnet')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('omw-1.4')

    # 首先，进行词性标注
    tagged_words = pos_tag(sum_list)

    # 定义一个函数，用于从 NLTK 的标签转换为 WordNet 的标签
    def get_wordnet_pos(treebank_tag):
        if treebank_tag.startswith('J'):
            return wordnet.ADJ
        elif treebank_tag.startswith('V'):
            return wordnet.VERB
        elif treebank_tag.startswith('N'):
            return wordnet.NOUN
        elif treebank_tag.startswith('R'):
            return wordnet.ADV
        else:
            return wordnet.NOUN  # 默认为名词
    def simple_end_s(processed_result):
        if processed_result.endswith("s"):
            processed_result=processed_result[:-1]
        return processed_result
    def remove_s(word):
        word=re.sub(r'\s*\([^)]*\)', '', word)
        # word=word.replace("  "," ")
        word=word.replace(".","").lower()

        lemmatizer = WordNetLemmatizer()
        words = word.split()  # 分割短语为单独的词

        singular_words = [lemmatizer.lemmatize(word) for word in words]  # 对每个词进行词形还原
        singular_words_removed_s=[simple_end_s(word) for word in singular_words]
        processed_result= ' '.join(singular_words_removed_s)
        if processed_result.endswith("s"):
            processed_result=processed_result[:-1]
        return processed_result
    sum_WithDuplicate_words = []
    for word, tag in tagged_words:
        wordnet_tag = get_wordnet_pos(tag)
        lemmatized_word = lemmatizer.lemmatize(word, wordnet_tag)

        sum_WithDuplicate_words.append(remove_s(lemmatized_word))
    #sum_WithDuplicate_words is the list of all words after cleaning (without removing duplicate)
    # 将集合转换为列表
    # word_counts = Counter(sum_WithDuplicate_words)

    # sorted_words = word_counts.most_common()

    sum_WithoutDuplicate = list(set(sum_WithDuplicate_words)) #已经去重，排序按照词频

    print("processed length: ",len(sum_WithoutDuplicate))
    model = SentenceTransformer('all-MiniLM-L6-v2')


    # text_labels = ["cat", "dog", "animal", "computer", "laptop", "pet", "gpt", "gpt-4", "gpt3.5", "openai",
    #                "microsoft company", "usa", "USA", "China", "England", "india", "woman", "sex", "traffic accident",
    #                "murder", "Apple company", "man", "life", "discrimination", "criminal", "sexual abuse"]
    sentence_embeddings = model.encode(sum_WithoutDuplicate)
    return sentence_embeddings,sum_WithoutDuplicate,sum_WithDuplicate_words
def calculate_tokens(string):
    if isinstance(string,list):
        string=" ".join(string)
    import tiktoken
    encoding = tiktoken.get_encoding("cl100k_base")
    # encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    num_tokens = len(encoding.encode(string))
    print(num_tokens)
def get_cluster_from_openai(file_path,top_words=None):
    cleaned_words=get_clean_word(file_path,top_words=None)
    import openai
    from sklearn.cluster import DBSCAN
    import numpy as np
    # 设置您的 OpenAI API 密钥
    openai.api_key = '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'

    def text_to_vector(text):
        response = openai.Embedding.create(
            input=text,
            engine="text-similarity-babbage-001"  # 您可以根据需要选择不同的模型
        )
        return response['data'][0]['embedding']

    # 示例文本标签列表
    # text_labels = ["cat", "dog", "animal", "computer", "laptop", "pet"]

    # 向量化所有标签
    # vectors = [text_to_vector(label) for label in text_labels]
    # 示例文本标签列表
    text_labels = ['gpt3.5', 'openai', 'microsoft', 'England', 'woman', 'sex', 'traffic accident', 'murder',
                   'Apple company', 'man', 'life', 'discrimination', 'sexual abuse']
    # text_labels = ["cat", "dog", "animal", "computer", "laptop", "pet","gpt","gpt-4","gpt3.5","openai","microsoft","usa","USA","china","England","india","woman","sex","traffic accident","murder","Apple company","man","life","discrimination","sexual abuse"]
    vectors = [text_to_vector(label) for label in cleaned_words]
    # 向量化所有标签
    dbscan = DBSCAN(eps=0.5, min_samples=2).fit(np.array(vectors))

    # 获取每个样本的聚类标签
    labels = dbscan.labels_

    # 创建一个字典，以聚类索引作为键，相应的文本标签列表作为值
    clusters = {}
    for label, text_label in zip(labels, cleaned_words):
        if label not in clusters:
            clusters[label] = []
        clusters[label].append(text_label)

    # 打印每个聚类的结果
    for cluster, texts in clusters.items():
        print(f"Cluster {cluster}: {texts}")
    #sorted_sum_lemmatized_list ： 按词频顺序排列的表
def get_cluster(sum_WithoutDuplicate, sentence_embeddings, eps, min_samples):
    # no_repeat_label_list=get_clean_word(file_path)
    # no_repeat_label_list=get_clean_word(r"C:\Users\Morning\Desktop\hiwi\heart\paper\hi_structure\sum_all_labels_hierarchy_labels.jsonl")


    # vectors = sentence_embeddings.tolist()
    # print(len(vectors))
    dbscan = DBSCAN(eps=eps, min_samples=min_samples).fit(sentence_embeddings)
    dbscan_labels = dbscan.labels_
    print(len(dbscan_labels))

    pca = PCA(n_components=3)
    compressed_embedding = pca.fit_transform(sentence_embeddings)
    label_embedding_pair = {}
    # 将压缩后的嵌入转换为列表并保存为JSON文件

    cluster_centers = {}
    for label in set(dbscan_labels):
        # if label != -1:  # 排除噪声点
            # 获取当前聚类的所有点
            members = sentence_embeddings[np.where(dbscan_labels == label)[0]]

            # 计算聚类中心
            center = members.mean(axis=0)
            cluster_centers[label] = center

    # 找出每个聚类中距离中心最近的点
    central_point_indices = {}
    for label, center in cluster_centers.items():
        # 获取当前聚类所有成员的索引
        member_indices = np.where(dbscan_labels == label)[0]
        # 计算到中心的距离
        distances = distance.cdist([center], sentence_embeddings[member_indices])[0]
        # 获取距离最近的点的索引
        central_point_index = member_indices[np.argmin(distances)]
        central_point_indices[label] = central_point_index

    print("central_point_indices",central_point_indices)
    compressed_embedding_list = compressed_embedding.tolist()
    for num, i in enumerate(compressed_embedding_list):
        label_embedding_pair[sum_WithoutDuplicate[num]] = i



    clusters = {}
    for label, text_label in zip(dbscan_labels, sum_WithoutDuplicate):
        if label not in clusters:
            clusters[label] = []
        clusters[label].append(text_label)
    print("length of cluster: ",len(clusters))
    pca_result_dict = {}

    for cluster, labels in clusters.items():
        cluster_center_label= str(cluster) +"_" + sum_WithoutDuplicate[central_point_indices[(cluster)]]
        pca_result_dict[cluster_center_label] = {}
        for item_ in label_embedding_pair:
            if item_ in labels:
                pca_result_dict[cluster_center_label].update({str(item_): label_embedding_pair[item_]})
        # if cluster==-1:
        #     print("len -1 cluster: ",len(labels))
        print(f"Cluster {cluster}: {len(labels)}")
    # print(pca_result_dict)
    # with open('compressed_embedding.json', 'w') as f:
    #     json.dump(pca_result_dict, f)
    return pca_result_dict
def make_alignment(pca_result_dict,sum_WithDuplicate_words):
    # aa={"1_cluster":{"a":[],"b":[],"c":[]},"2_ccc":{"aa":[],"vv":[],"cc":[]}}
    raw_list=sum_WithDuplicate_words.copy()
    for cluster_key in pca_result_dict:
        for word in pca_result_dict[cluster_key].keys():
            raw_list = [cluster_key.split("_")[1] if item == word else item for item in raw_list]

    word_counts = Counter(raw_list)
    print(word_counts)

    sorted_sum_list = sorted(word_counts, key=lambda x: (-word_counts[x], x))
    print(len(sorted_sum_list),"len(sorted_sum_list)")
    return sorted_sum_list,raw_list

#
# sentence_embeddings,sum_WithoutDuplicate,sum_WithDuplicate_words=get_clean_word(r"C:\Users\Morning\Desktop\hiwi\heart\paper\hi_structure\sum_all_labels_hierarchy_labels.jsonl")
# pca_result_dict=get_cluster(sum_WithoutDuplicate,sentence_embeddings,0.5,2)
# sorted_sum_list,raw_list=make_alignment(pca_result_dict,sum_WithDuplicate_words)


# calculate_tokens(num_list)
# get_cluster(num_list)
# print(get_clean_word(""))