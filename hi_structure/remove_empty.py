# 指定原始JSONL文件和要写入的新文件
original_file_path = 'original_file.jsonl'
cleaned_file_path = 'cleaned_file.jsonl'

# 打开原始文件以读取，打开新文件以写入
with open(original_file_path, 'r') as infile, open(cleaned_file_path, 'w') as outfile:
    for line in infile:
        # 检查行是否非空（跳过空行）
        if line.strip():
            # 将非空行写入新文件
            outfile.write(line)

# 完成后，'cleaned_file.jsonl' 将不包含任何空行
