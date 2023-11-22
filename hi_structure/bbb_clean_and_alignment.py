from collections import Counter
import json
from sklearn.cluster import DBSCAN
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA
import json
from sentence_transformers import SentenceTransformer
# Load the JSONL file
def get_clean_word(file_path,top_words=None):
    # file_path = 'output_labels_list.jsonl'

    # Read and parse the JSONL file
    with open(file_path, 'r') as file:
        # Read the lines in the file
        lines = file.readlines()
        # Parse each line as a JSON object
        data = [json.loads(line) for line in lines]

    # Initialize a Counter object to hold the word frequencies
    word_freq = Counter()


    # Initialize the WordNet lemmatizer
    sum_set=set()
    sum_list=[]

    for entry in data:
        word_list = entry['label_list']
        for word in word_list:
            sum_set.add(word)
        sum_list.extend(word_list)
        # Update the word frequencies
        word_freq.update(word_list)
    print("original length:",len(sum_list))
    print("original no repeat length:", len(sum_set))
    # all_word_list_before_clean_num = sum(1 for word, freq in word_freq.items() if freq == 1)
    # print(all_word_list_before_clean_num)
    from nltk.stem import WordNetLemmatizer

    # 初始化词形还原器
    lemmatizer = WordNetLemmatizer()

    import nltk
    from nltk.corpus import wordnet
    from nltk.tag import pos_tag

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

    no_repeat_lemmatized_words = set()
    sum_lemmatized_words = []
    for word, tag in tagged_words:
        wordnet_tag = get_wordnet_pos(tag)
        lemmatized_word = lemmatizer.lemmatize(word, wordnet_tag)
        no_repeat_lemmatized_words.add(lemmatized_word)
        sum_lemmatized_words.append(lemmatized_word)
    # 将集合转换为列表
    word_counts = Counter(sum_lemmatized_words)
    lemmatized_list = list(no_repeat_lemmatized_words)
    sorted_words = word_counts.most_common()
    # print("sorted_words:",sorted_words)
    sorted_sum_lemmatized_list = [word for word, count in sorted_words] #已经去重，排序按照词频
    # print(sorted_sum_lemmatized_list)
    print("processed length: ",len(sorted_sum_lemmatized_list))
    return sorted_sum_lemmatized_list
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
def get_cluster(text_labels):

    model = SentenceTransformer('all-MiniLM-L6-v2')


    # text_labels = ["cat", "dog", "animal", "computer", "laptop", "pet", "gpt", "gpt-4", "gpt3.5", "openai",
    #                "microsoft company", "usa", "USA", "China", "England", "india", "woman", "sex", "traffic accident",
    #                "murder", "Apple company", "man", "life", "discrimination", "criminal", "sexual abuse"]
    sentence_embeddings = model.encode(text_labels)
    vectors = sentence_embeddings.tolist()
    print(len(vectors))

    pca = PCA(n_components=3)
    compressed_embedding = pca.fit_transform(np.array(vectors))
    first_dict = {}
    # 将压缩后的嵌入转换为列表并保存为JSON文件
    compressed_embedding_list = compressed_embedding.tolist()
    for num, i in enumerate(compressed_embedding_list):
        first_dict[text_labels[num]] = i

    dbscan = DBSCAN(eps=0.7, min_samples=2).fit(np.array(vectors))

    # 获取每个样本的聚类标签
    labels = dbscan.labels_

    # 创建一个字典，以聚类索引作为键，相应的文本标签列表作为值
    clusters = {}
    for label, text_label in zip(labels, text_labels):
        if label not in clusters:
            clusters[label] = []
        clusters[label].append(text_label)
    result_dict = {}
    # 打印每个聚类的结果
    for cluster, labels in clusters.items():
        result_dict[str(cluster)] = {}
        for item_ in first_dict:
            if item_ in labels:
                result_dict[str(cluster)].update({str(item_): first_dict[item_]})
        print(f"Cluster {cluster}: {labels}")
    print(result_dict)
    with open('compressed_embedding.json', 'w') as f:
        json.dump(result_dict, f)


num_list=get_clean_word(r"C:\Users\Morning\Desktop\hiwi\heart\paper\hi_structure\sum_all_labels_hierarchy_labels.jsonl")
# calculate_tokens(num_list)
get_cluster(num_list)
# print(get_clean_word(""))