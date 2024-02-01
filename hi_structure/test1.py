import os

def delete_files_ending_with_qqq(directory):
    # 遍历指定目录下的所有文件和文件夹
    for filename in os.listdir(directory):
        # 构造完整的文件路径
        file_path = os.path.join(directory, filename)
        # 检查这是一个文件且文件名以"qqq"结尾
        if os.path.isfile(file_path) and filename.endswith("profile_complete.jsonl"):
            # 删除文件
            os.remove(file_path)
            print(f"Deleted: {file_path}")

# 指定要清理的目录路径
directory_path = r"C:\Users\Morning\Desktop\hiwi\heart\paper\hi_structure\twitter_data2"
delete_files_ending_with_qqq(directory_path)
