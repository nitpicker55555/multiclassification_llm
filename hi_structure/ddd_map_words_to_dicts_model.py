# from gpt_api_singel import change_statement
import json
import os

from transformers import pipeline
from tqdm import tqdm
import torch
if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")
    print("CUDA is not available. Using CPU...")

def with_model(key_labels,candidate_labels):


    # 初始化zero-shot分类器
    classifier = pipeline('zero-shot-classification', model='roberta-large-mnli', device=device)


    # sequence_to_classify = "I want to search buildings in the farmland"
    # candidate_labels = ['general buildings', 'land use', "specific type of buildings"]

    # 对每个标签独立评估
    results = {}
    for label in candidate_labels:
        results[label] = []
        for label_ in  tqdm(key_labels, desc=label):

            # 用每个候选标签和一个通用负面标签（如"无关"）进行比较
            hypothesis_template = "This text is about {}."
            labels_to_test = [label, "Not Relevant"]
            try:
                output = classifier(label_, labels_to_test, hypothesis_template=hypothesis_template,
                                multi_label=True)
                label_score = output['scores'][0] if output['labels'][0] == label else output['scores'][1]
                if label_score > 0.9:
                    # print(label_,label)

                    results[label].append(label_)
            except:
                print(label_," ",label)
            # 保存和对比置信度


    return (results)


def map_words_2_dicts(json_structure,all_list,filename):


  def get_bottom_keys(nested_dict,result_list):
      """
      get all bottom keys return as {key:{}}

      {'Madigan Army Medical Center': [], 'Tacoma': [], '5-2 Infantry': [], 'Iraq Deployment': [], 'Afghanistan Deployment': [], 'Wartime Atrocities': [], 'British Army': [], 'Lewis-McChord': [], 'British Society and Military': [], 'Gulf War': [], 'Student-Led Initiatives': [], 'Environmental Movement': [], 'Green Schools': [], 'Environmental Impact': [], 'Geography Curriculum': [], 'Sustainable Development': [], 'Western Capital': [], 'Geographic Location': [], 'Aid Work': [], 'Western Organizations': [], 'Management and Experience': [], 'Neo-Colonialism': [], 'machine learning': [], 'large-language model': [], 'Automation and Employment': [], 'Geographic Information Systems': [], 'Encryption and Data Protection': [], 'Technology Procurement': [], 'Religious Education': [], 'Gender Identity': [], 'Socialization and Independence': [], 'Political Funding': [], 'Public Service': [], 'Transgender Rights': [], 'Climate Debt': [], 'Carbon Tax': [], 'Renewable Energy': [], 'Carbon Footprint': [], 'Sustainable Fashion': [], 'Green Technologies': []}

      :param dict_:
      :return:
      """

      def recurse(element):
          if isinstance(element, dict):
              # 对于字典中的每个键值对，递归调用
              for key, value in element.items():
                  recurse(value)
          elif isinstance(element, list):
              # 如果元素是列表，则输出
              result_list.extend(element)
              # print(result_list)

      recurse(nested_dict)
      result_dict = {}
      for i in set(result_list):
          result_dict[i] = []
      return (result_dict)

  try:
    with open("tem_file/mapped_dicts_%s"%filename, 'r') as f:
      mapped_dicts = json.load(f)
      print("mapped_dicts exist",mapped_dicts)
  except:
      # all_list=get_clean_word(file_path)
      bottom_keys=get_bottom_keys(json_structure,[])

      mapped_dicts=with_model(all_list[:500],bottom_keys)
      with open("tem_file/mapped_dicts_%s"%filename, 'w', encoding='utf-8') as file:
        json.dump(mapped_dicts, file)
  return mapped_dicts
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
    with open("tem_file/json_structure_%s"%file_name, "r") as file:
        json_structure = json.load(file)
    map_words_2_dicts(json_structure,loaded_list,file_name)