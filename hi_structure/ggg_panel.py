import subprocess
from tqdm import tqdm
import os


def run_process(py_file,folder_path):
    # folder_path = "twitter_files"
    task_list=[]
    # 使用os.walk遍历文件夹内的文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith("_labels.jsonl") and not file.endswith("_hierarchy_labels.jsonl") :
                file_path = os.path.join(root, file)
                print(file_path)
                task_list.append(file_path)
    print("Task length:" ,len(task_list))
    for file in tqdm(task_list, desc=py_file.replace(".py","")):
        command = ["python", py_file, "--file_path", file]
        # 调用另一个脚本
        subprocess.run(command)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Example Script with Named Arguments')
    parser.add_argument('--py_file', type=str, help='py_file')
    parser.add_argument('--folder', type=str, help='folder')
    args = parser.parse_args()
    run_process(args.py_file,args.folder)

