import os
import shutil

# 定义文件夹路径
source_dir = 'chart'
destination_dir = 'chart2'

# 获取所有的png文件并排序
file_list = sorted([f for f in os.listdir(source_dir) if f.endswith('.png')])

# 按照名称顺序从小到大重命名并复制到chart2文件夹
for index, filename in enumerate(file_list, start=1):
    source_path = os.path.join(source_dir, filename)
    destination_path = os.path.join(destination_dir, f"{index}.png")
    shutil.copy2(source_path, destination_path)
    print(f"Copy {filename} to {destination_path}")

print("All files have been renamed and copied.")
