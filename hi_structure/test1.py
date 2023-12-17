def find_bottom_lists(nested_dict,result_list):
    # 定义一个内部递归函数
    # result_list=[]
    def recurse(element):
        if isinstance(element, dict):
            # 对于字典中的每个键值对，递归调用
            for key, value in element.items():
                recurse(value)
        elif isinstance(element, list):
            # 如果元素是列表，则输出
            result_list.extend(element)
            # print(result_list)

    recurse(nested_dict)
    result_dict={}
    for i in set(result_list):
        result_dict[i]=[]
    return (result_dict)

# 示例嵌套字典

nested_dict = {
    'a': [1, 2, 3],
    'b': {'x': [2, 2, 6], 'y': 'not a list', 'z': {'p': [7, 8, 9]}},
    'c': 'not a list or dict'
}

# 调用函数
print(find_bottom_lists(nested_dict,[]))
