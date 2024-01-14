import os
import json

def find_sorted_jsonl_files(path):
    """
    遍历指定路径，寻找所有以'sorted'开头的.jsonl文件。
    """
    if not os.path.exists(path):
        print(f"路径不存在: {path}")
        return []

    for file in os.listdir(path):
        if file.startswith("sorted") and file.endswith("merged_output.jsonl"):
            yield os.path.join(path, file)

def read_jsonl_file(file_path, limit=700):
    """
    读取jsonl文件的前limit个元素。
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            loaded_list = json.load(file)
        return (loaded_list[:limit])
    except Exception as e:
        print(f"读取文件时出错: {e}")

def is_valid_json(json_str):
    """
    检查字符串是否是有效的JSON。
    """
    try:
        json.loads(json_str)
        return True, None  # 当JSON有效时，返回True和None
    except json.JSONDecodeError as e:
        return False, str(e)  # 当JSON无效时，返回False和错误信息

def get_user_json():
    """
    获取用户输入的多行JSON，并检查其有效性。
    """
    print("请输入一个JSON结构 (多行), 然后输入'END'结束:")
    input_lines = []
    while True:
        line = input()
        if line == 'END':
            break
        input_lines.append(line)
    json_str = '\n'.join(input_lines)

    is_valid, error = is_valid_json(json_str)  # 获取两个返回值
    if is_valid:
        return json_str
    else:
        print(f"JSON结构错误: {error}")
        return None

def main():
    path = r"C:\Users\Morning\Desktop\hiwi\heart\paper\hi_structure\tem_file"   # 替换为你的路径
    for jsonl_file in find_sorted_jsonl_files(path):
        print(f"处理文件: {jsonl_file}")
        print( read_jsonl_file(jsonl_file))

        while True:
            user_json = get_user_json()
            if user_json:
                with open(jsonl_file.replace("sorted_word_list","json_structure"), 'a', encoding='utf-8') as f:
                    f.write(user_json + '\n')
                break

if __name__ == "__main__":
    main()

