from nltk.stem import WordNetLemmatizer
from collections import Counter
# 初始化词形还原器
lemmatizer = WordNetLemmatizer()

import nltk
from nltk.corpus import wordnet
from nltk.tag import pos_tag

# 确保已下载所需的 NLTK 资源
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('omw-1.4')

# 重新定义词汇列表
words = ['apples', 'cccc','apple', 'binaries', 'binary','running','apple']

# 首先，进行词性标注
tagged_words = pos_tag(words)

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

# 对每个词进行词形还原
lemmatized_words = set()
sum_list=[]
for word, tag in tagged_words:
    wordnet_tag = get_wordnet_pos(tag)
    lemmatized_word = lemmatizer.lemmatize(word, wordnet_tag)
    lemmatized_words.add(lemmatized_word)
    sum_list.append(lemmatized_word)
word_counts = Counter(sum_list)
sorted_words = word_counts.most_common()
# 将集合转换为列表
lemmatized_list = list(lemmatized_words)
print(lemmatized_list)
print(sum_list)
print(sorted_words)
sorted_word_list = [word for word, count in sorted_words]
print(sorted_word_list)