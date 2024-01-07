import subprocess
from tqdm import tqdm
import os


def run_process(py_file,folder_path):
    # python aaa_model_set_label.py --file_path twitter_files\2019-1-1_2019-12-31_without_profile.jsonl --col_name content --thread_num 10
    # python bbb_clean_and_alignment.py --file_path twitter_files\2019-1-1_2019-12-31_without_profile.jsonl --min_samples 3
    # python fff_sentiment_analyse.py --file_path twitter_files\2018-1-1_2018-12-31_without_profile.jsonl --col_name content --thread_num 10
    # folder_path = "twitter_files"
    task_list=[]
    # 使用os.walk遍历文件夹内的文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # if file.endswith("_profile.jsonl")  :
            if file.endswith("_merged_output.jsonl")  :
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

