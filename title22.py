import json
import re

text = """Based on the provided information, it is not clear whether there is a privacy violation in the news. Privacy violations typically involve the unauthorized or inappropriate disclosure of personal information. The information provided in the news article does not explicitly mention a privacy violation. Therefore, the answer is:
asd
{
  "Boolean_value": true,
  "asd": false
}
asd
"""

# 使用正则表达式提取JSON字符串
# 这个正则表达式试图匹配从 '{' 开始，到 '}' 结束的内容
match = re.search(r'({[^{}]*})', text)
json_str = match.group(1) if match else None

if json_str:
    dictionary = json.loads(json_str)

    for i in dictionary:
        if dictionary[i]==True:
            print(dictionary.keys())
else:
    print("在文本中未找到JSON字符串。")
