from collections import Counter
aa = {"1_cluster": {"a": [], "b": [], "c": []}, "2_ccc": {"aa": [], "vv": [], "cc": []}}
raw_list = ["a", "b", "c", "c", "c", "aa", "aa", "aa", "aa", "aa", "aa", 'vv', 'cc','asdas']
for i in aa:
    for word in aa[i].keys():

        raw_list = [ i if item == word else item for item in raw_list]
word_counts = Counter(raw_list)

# 根据出现频率对元素进行排序
# 这将按频率降序排序；如果频率相同，则按字母顺序排序
sorted_words = sorted(word_counts, key=lambda x: (-word_counts[x], x))
print(sorted_words)