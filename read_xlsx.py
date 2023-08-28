import pandas as pd

# 读取.xlsx文件
file_path = 'Geo-AI ethics cases(1).xlsx'
df = pd.read_excel(file_path, engine='openpyxl')

# 创建一个空列表存放提取的数据
data_list = []

# 通过行迭代，提取每行的 '标题列'、'说明列' 和 '详细描述列' 的数据
for _, row in df.iterrows():
    title = row['标题']
    description = row['说明']
    details = row['详细描述']

    # 将这三个数据元素添加到一个新的列表中
    data_list.append([title, description, details])

# 输出结果
print(data_list)
