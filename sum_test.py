import os,json,glob
import pandas as pd
start_directory='.'
for folder in glob.glob(os.path.join(start_directory, 'content_*')):
    if os.path.isdir(folder):
        for folder in glob.glob(os.path.join(start_directory, 'content_*')):
            if os.path.isdir(folder):
                # 在每个 'content_' 文件夹中，查找所有以 'updated_file' 开头的 .xlsx 文件
                for excel_file in (glob.glob(os.path.join(folder, 'updated_file*.xlsx'))):
                    jsonl_file_path=excel_file.replace(".xlsx","classification_result_json.jsonl")
                    if os.path.exists(jsonl_file_path):
                        with open(jsonl_file_path, 'r') as f:
                            content = f.read()
                            # 检查是否存在"finish"字符
                        if "Finish_json_file" not in content:
                            df = pd.read_excel(excel_file, engine='openpyxl')

                            overview_column = df['Overview']
                            true_col = df['Relevant']
                            num_col = df['num']
                            # print(true_col)
                            threads = []
                            row_nums = []
                            # 解析JSONL文件内容
                            for line in content.splitlines():
                                data = json.loads(line)
                                if "row_num" in data:
                                    row_nums.append(str(data["row_num"]))
print(row_nums)