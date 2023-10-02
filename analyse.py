import os

# 获取当前工作目录
current_dir = os.getcwd()

# 初始化一个字典来存储每个文件夹中'Is_relevant=True'的数量
folder_count = {}

# 遍历当前目录下的每个以"content"开头的文件夹
for folder in os.listdir(current_dir):
    if folder.startswith('content_') and os.path.isdir(folder):

        folder_path = os.path.join(current_dir, folder)
        count = 0
        num_cases=0
        # 遍历文件夹中的每个txt文件
        for file in os.listdir(folder_path):
            if file.endswith('.txt'):
                file_path = os.path.join(folder_path, file)

                # 读取文件内容并计算'Is_relevant=True'的数量
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    count += content.count('Is_relevant": false')

                    num_cases+=content.count('__________________________________________________')

        # 将计算结果存储到字典中
        print(folder,"---------------",num_cases)
        folder_count[folder] =num_cases- count

for folder, count in folder_count.items():
    print(f'{folder}: {count}')
print(folder_count)
print(sum(folder_count.values()))