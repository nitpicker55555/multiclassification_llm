# 标签及其相似标签的数据
label_data = {
    "cat": ["dog", "animal", "pet"],
    "dog": ["cat", "animal", "pet"],
    "animal": ["cat", "dog", "pet"],
    "computer": ["laptop", "openai", "microsoft"],
    "laptop": ["computer"],
    "pet": ["cat", "dog", "animal", "gpt"],
    "gpt": ["pet", "gpt-4", "gpt3.5"],
    "gpt-4": ["gpt", "gpt3.5"],
    "gpt3.5": ["gpt", "gpt-4"],
    "openai": ["computer"],
    "microsoft": ["computer"]
}

# 创建一个字典来存储不重复的标签组
unique_groups = {}

# 为每个标签及其相似标签创建组
for label, similar_labels in label_data.items():
    # 检查标签是否已经存在于某个组中
    existing_group = None
    for group, members in unique_groups.items():
        if label in members:
            existing_group = group
            break

    # 如果标签已经存在于一个组中，则将其相似标签添加到该组
    if existing_group is not None:
        unique_groups[existing_group].update(similar_labels)
    else:
        # 否则，为该标签创建一个新组
        unique_groups[label] = set(similar_labels + [label])

# 清理组，删除重复的标签
for group, members in unique_groups.items():
    unique_groups[group] = sorted(list(members))

# 将结果转换为列表格式
grouped_labels = list(unique_groups.values())

print(grouped_labels)

