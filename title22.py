original_list = ["apple", "banana", "cherry date", "fig", "grape"]

# 使用列表推导式分割含有空格的元素并组合成一个大列表
split_and_combined_list = [word.split() if ' ' in word else [word] for word in original_list]

# 将嵌套的列表展平
flattened_list = [item for sublist in split_and_combined_list for item in sublist]

print(flattened_list)
