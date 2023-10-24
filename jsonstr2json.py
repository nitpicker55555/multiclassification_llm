import re
import json

def json_transfer_func(s):
    s=str(s)
    # 使用正则表达式来匹配字典格式的字符串
    match = re.search(r"{.*?}", s, re.DOTALL)

    # 如果匹配成功，提取字典字符串并转换为JSON格式
    if match:
        dict_str = match.group(0)

        # 替换单引号为双引号
        dict_str = dict_str.replace("'", '"')

        # 使用json.loads加载为字典
        dictionary = json.loads(dict_str)
        return dictionary
    else:
        return ""