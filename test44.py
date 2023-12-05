import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def capitalize_content_words(text):

    # 词性标记
    words = word_tokenize(text)
    tagged = nltk.pos_tag(words)

    # 定义实词词性标记（名词、动词、形容词、副词）
    content_word_tags = {'NN', 'NNS', 'NNP', 'NNPS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS'}

    # 将实词首字母大写
    capitalized_words = [word.capitalize() if tag in content_word_tags else word for word, tag in tagged]
    return ' '.join(capitalized_words)

# 示例
result_lines=[]

for i in lines:
    small_list = []
    for ii in i:
        small_list.append(capitalize_content_words(ii))
    result_lines.append(small_list)
print(result_lines)
