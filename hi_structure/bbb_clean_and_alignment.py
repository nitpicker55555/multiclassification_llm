from collections import Counter
import json

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

    sum_list=[]
    for entry in data:
        word_list = entry['label_list']
        sum_list.extend(word_list)
        # Update the word frequencies
        word_freq.update(word_list)
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

    sorted_sum_lemmatized_list = [word for word, count in sorted_words]
    print(sorted_sum_lemmatized_list)
    return sorted_sum_lemmatized_list
    #sorted_sum_lemmatized_list ： 按词频顺序排列的表

# print(get_clean_word(""))