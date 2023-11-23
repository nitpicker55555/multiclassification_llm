import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')

def plural_to_singular_nltk(word):
    lemmatizer = WordNetLemmatizer()
    words = word.split()  # 分割短语为单独的词
    singular_words = [lemmatizer.lemmatize(word) for word in words]  # 对每个词进行词形还原
    return ' '.join(singular_words)  # 将还

# 测试
words = ['buses', 'parties', 'passenger injuries', 'knives', 'boys', 'glasses']
singular_words = [plural_to_singular_nltk(word) for word in words]
print(singular_words)
