# from bbb_clean_and_alignment import get_clean_word
from gpt_api_singel import change_statement
def get_structure(sorted_sum_lemmatized_list):

    # sorted_sum_lemmatized_list=get_clean_word(file_name)
    # sorted_sum_lemmatized_list=get_clean_word(r'C:\Users\Morning\Desktop\hiwi\heart\paper\hi_structure\sum_all_labels.jsonl')
    print(len(sorted_sum_lemmatized_list))
    system_content='I have a list of words and I need you to Abstract a hierarchical tag structure from this word list. Please return the structure in JSON format'
    user_content=sorted_sum_lemmatized_list[:500]
    result_structure=change_statement(system_content,user_content,"4")
    print(isinstance(result_structure,dict))
    print(result_structure)
    return result_structure