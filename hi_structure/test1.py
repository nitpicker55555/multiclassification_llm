import json
label_set= {}
num_list=[]
sentiment={}
sentiment_analyse={}
from collections import Counter

def calculate_proportions(lst):
    count = Counter(lst)
    total = len(lst)
    proportions = {element: round(count[element] / total, 4) for element in count}
    return proportions
with open(r"C:\Users\Morning\Desktop\hiwi\heart\paper\hi_structure\uploads\example_sentiment.jsonl", 'r') as file:
    for line in (file):
        json_obj = json.loads(line)
        sentiment[json_obj['num']]=list(json_obj['sentiment'].keys())[0]
with open(r"C:\Users\Morning\Desktop\hiwi\heart\paper\hi_structure\uploads\example_labels.jsonl", 'r') as file:
    for line in (file):
        json_obj = json.loads(line)
        for i in json_obj['label_list']:
            if i not in label_set:
                label_set[i]= {}
            if sentiment[json_obj['num']] not in label_set[i]:
                label_set[i][sentiment[json_obj['num']]]=0
            label_set[i][sentiment[json_obj['num']]]+=1
def sum_values(nested_dict):
    return sum(nested_dict.values())
print()
sorted_data = dict(sorted(label_set.items(), key=lambda item: sum_values(item[1]), reverse=True))
print(calculate_proportions(sentiment.values()))
print(sentiment)
print(str(sorted_data))
with open(r"example_sentiment_result.jsonl", 'a') as f:
    json_str = json.dumps(sorted_data)
    f.write(json_str + '\n')
with open(r"example_sentiment_result.jsonl", 'a') as f:
    json_str = json.dumps(calculate_proportions(sentiment.values()))
    f.write(json_str + '\n')

