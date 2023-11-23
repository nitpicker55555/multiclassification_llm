from gpt_api_singel import change_statement

json_structure={
  "Military and Conflict": {

    "War and Deployment": {
      "Medical Center",
      "Military Deployment",
      "Wartime Atrocities",
      "Army",
      "War"
    },

  },
  "Environment and Education": {
    "School Projects": {
      "Green Schools",
      "Student-Led Initiatives",
      "Environmental Movement"
    },
    "Geography Education": {
      "Sustainable Development",
      "Geography Curriculum",
      "Environmental Impact"
    }
  },
  "Humanitarianism and Development": {
    "International Aid": {
      "Aid Work",
      "Western Capital",
      "Geographic Location"
    },
    "Humanitarian Field": {
      "Neo-Colonialism",
      "Management and Experience",
      "Western Organizations"
    }
  },
  "Technology and Innovation": {
    "Artificial Intelligence": {
      "large-language model",
      "Automation and Employment",
      "machine learning"
    },
    "Data and Geographic Information": {
      "Encryption and Data Protection",
      "Geographic Information Systems",
      "Technology Procurement"
    }
  },
  "Politics and Social Issues": {
    "Tradition and Modern Views": {
      "Gender Identity",
      "Religious Education",
      "Socialization and Independence"
    },
    "Policy and Legislation": {
      "Transgender Rights",
      "Political Funding",
      "Public Service"
    }
  },
  "Climate Change and Sustainability": {
    "Climate Justice": {
      "Carbon Tax",
      "Climate Debt",
      "Renewable Energy"
    },
    "Environmental Initiatives": {
      "Green Technologies",
      "Sustainable Fashion",
      "Carbon Footprint"
    }
  }
}
def map_words_2_dicts(json_structure,all_list):
  def merge_dictionaries(dict_list):
    """

    :param dict_list:  all seperate dict
    :return:
    """
    merged_dict = {}
    for dictionary in dict_list:
      for key, value in dictionary.items():
        if key in merged_dict:
          # 如果键已存在，合并列表
          merged_dict[key] += value
        else:
          # 如果键不存在，直接添加键和值
          merged_dict[key] = value
    return merged_dict
  def get_bottom_keys(dict_):
      """
      get all bottom keys return as {key:{}}

      {'Madigan Army Medical Center': [], 'Tacoma': [], '5-2 Infantry': [], 'Iraq Deployment': [], 'Afghanistan Deployment': [], 'Wartime Atrocities': [], 'British Army': [], 'Lewis-McChord': [], 'British Society and Military': [], 'Gulf War': [], 'Student-Led Initiatives': [], 'Environmental Movement': [], 'Green Schools': [], 'Environmental Impact': [], 'Geography Curriculum': [], 'Sustainable Development': [], 'Western Capital': [], 'Geographic Location': [], 'Aid Work': [], 'Western Organizations': [], 'Management and Experience': [], 'Neo-Colonialism': [], 'machine learning': [], 'large-language model': [], 'Automation and Employment': [], 'Geographic Information Systems': [], 'Encryption and Data Protection': [], 'Technology Procurement': [], 'Religious Education': [], 'Gender Identity': [], 'Socialization and Independence': [], 'Political Funding': [], 'Public Service': [], 'Transgender Rights': [], 'Climate Debt': [], 'Carbon Tax': [], 'Renewable Energy': [], 'Carbon Footprint': [], 'Sustainable Fashion': [], 'Green Technologies': []}

      :param dict_:
      :return:
      """
      new_dict = {}
      for category in dict_:
          for subcategory in dict_[category]:
              for item in dict_[category][subcategory]:
                  new_dict[item] = []
      return new_dict
  # all_list=get_clean_word(file_path)
  bottom_keys=get_bottom_keys(json_structure)
  system_content="Please assign the following words to the corresponding categories. Add each keyword to the key-value list of its category and return it in JSON format. The following is optional categories and the list of keywords to be classified: "+"optional_categories="+str(bottom_keys)
  final_dict_list=[]
  for i in range(0, len(all_list), 50):
    if i <600:
      print(i)
      split_all_list= all_list[i:i + 50]
      print(system_content)
      print(split_all_list)
      print("============================")
      final_dict=change_statement(system_content, split_all_list)

      print(final_dict)
      final_dict_list.append((final_dict))
      print("============================")
  print(merge_dictionaries(final_dict_list))
  return merge_dictionaries(final_dict_list)
#生成merged映射字典