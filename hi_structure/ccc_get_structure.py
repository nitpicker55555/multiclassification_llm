# from bbb_clean_and_alignment import get_clean_word
import os

from gpt_api_singel import change_statement
import json
def get_structure(sorted_sum_list,filename):
    try:
        with open('tem_file/json_structure_%s'%filename, 'r') as f:
            json_structure = json.load(f)
            print("json_structure exist",json_structure)
    except:

        # sorted_sum_lemmatized_list=get_clean_word(file_name)
        # sorted_sum_lemmatized_list=get_clean_word(r'C:\Users\Morning\Desktop\hiwi\heart\paper\hi_structure\sum_all_labels.jsonl')
        print(len(sorted_sum_list))
        system_content='I have a list of words and I need you to Abstract a hierarchical tag structure from this word list. Please return the structure in JSON format'
        user_content= sorted_sum_list[:500]
        json_structure=change_statement(system_content,user_content,"4")
        print(isinstance(json_structure,dict))
        print(json_structure)
        with open('tem_file/json_structure_%s'%filename,'w',encoding='utf-8') as file:
            json.dump(json_structure, file)
    return json_structure
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Example Script with Named Arguments')


    parser.add_argument('--file_path', type=str, help='file_path')
    # parser.add_argument('--min_samples', type=int, help='min_samples')
    # parser.add_argument('--thread_num', type=int, help='thread_num')
    # parser.add_argument('--max_out_put_length', type=int, help='max_out_put_length')
    # parser.add_argument('--num_beams', type=int, help='num_beams')
    args = parser.parse_args()
    file_name = os.path.basename(args.file_path)
    with open("tem_file/sorted_word_list_%s"%file_name, "r") as file:
        loaded_list = json.load(file)
    get_structure(loaded_list,file_name)