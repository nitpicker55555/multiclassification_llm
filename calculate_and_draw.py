data_structure={
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
def calculate_and_draw_func(data_structure,merged_dict,file_path):
    def convert_bottom_key_to_0(input_dict):
      for key, value in input_dict.items():
        if isinstance(value, set):
          # Convert set to dictionary with values set to 0
          input_dict[key] = {item: 0 for item in value}
        elif isinstance(value, dict):
          # Recursively call the function for nested dictionaries
          convert_bottom_key_to_0(value)
      return input_dict
    data_structure = convert_bottom_key_to_0(data_structure)
    # merged_dict={'Army': ['rogue base', '2-3 infantry', 'court-martial', 'leadership issue', 'british military', 'colonel blimp', "dad's army", 'us assessment', 'military prestige', 'us soldier', 'uk soldier', 'military budget', 'military history', 'military stereotype', 'finest hour', 'world war ii', 'waterloo', '5th stryker brigade', 'afghan civilian', 'kandahar', 'shooting', 'stryker brigade', 'iraq tour', 'scandal', 'national park', 'army medical', 'veteran', 'stress management', 'rampage', 'texa', 'gun right', 'ministry of defence', 'cadet force', 'british armed force'], 'Wartime Atrocities': ['wartime atrocitie', 'premeditated murder', '2010 murder', 'weekend rampage', 'guardian report', 'afghan civilian', 'kandahar', 'shooting', 'stryker brigade', 'iraq tour', 'scandal', 'conflict'], 'Medical Center': ['madigan army medical center', 'army medical', 'veteran', 'stress management'], 'War': ['iraq deployment', 'afghanistan deployment', 'gulf war', 'iraq war', '5th stryker brigade', 'afghan civilian', 'kandahar', 'shooting', 'stryker brigade', 'iraq tour', 'scandal'], 'Military Deployment': ['u.s. military', '5th stryker brigade', 'afghan civilian', 'kandahar', 'shooting', 'stryker brigade', 'iraq tour', 'nuclear disarmament', 'cnd', 'hiroshima', 'trident', 'university college', 'external speaker', 'forceswatch', 'child right', 'military etho', 'conflict resolution', 'peer mediation', 'jeremy corbyn', 'labour party'], 'Student-Led Initiatives': ['student-led', 'rachel pickering', 'henry greenwood', 'kingsmead school', 'eco-school', 'solar panel', 'green flag', 'student advice', "students' reaction"], 'Green Schools': ['green school', 'kingsmead school', 'eco-school', 'scottish green'], 'Environmental Movement': ['environmental issue', 'global citizenship', 'environmentalist', 'greenwashing', 'carbon-offsetting', 'fly responsibly', 'greenhouse gas', 'co2zero', 'reforestation', 'biofuel', 'consumer protection', 'prediction', 'mapping', 'green movement', 'leap manifesto', 'climate justice', 'racial injustice', 'intersectional response', 'overconsumption', 'heat dome', 'loss and damage agreement'], 'Sustainable Development': ['sustainability', 'sustainable development', 'development professional'], 'Geography Curriculum': ['geography', 'curriculum', 'human geography', 'geographical association', 'sqa', 'geography course', 'world map', 'mercator projection', 'peters projection', 'cartography', 'distortion', 'geography curriculum', 'teacher', 'government', 'national curriculum', 'environmental education', 'draft guideline', 'carbon dioxide', 'green education', 'science uncertainty', 'key stage', 'green technologie', 'oxfam', 'physical geography', 'locational knowledge', 'guardian professional', 'geographical processe', 'peace education'], 'Environmental Impact': ['climate change', 'global warming', 'fossil fuel', 'development', 'economic impact', 'environmental audit', 'recycling', 'environmental impact', 'leap manifesto', 'climate justice', 'racial injustice', 'intersectional response', 'overconsumption', 'heat dome', 'loss and damage agreement'], 'Aid Work': ['humanitarian', 'field', 'aid work', 'hurricane katrina'], 'Western Capital': ['western capital'], 'Geographic Location': ['tacoma', 'european union', 'eastern europe', 'amsterdam', 'netherlands', 'kandahar province', 'hong kong', 'manchester', 'hackney', 'canada', 'university of british columbia', 'british columbia', 'egypt', 'united arab emirate', 'geo group', 'georgia', 'charlton county', 'japan', 'russia', 'poland', 'nedo', 'hangary', 'spain', 'belgium', 'old soviet union', 'latvia', 'ukraine', 'czech', 'bulgaria', 'montana', 'oklahoma city', 'istanbul'], 'Neo-Colonialism': ['neo-colonial'], 'Management and Experience': ['leadership problem', 'chain of command', 'leadership', 'jennifer mcbride', 'stress-management', 'management', 'experience', 'coalition building', 'house committee', 'state administration', 'government budget'], 'Western Organizations': ['reuter', 'thomson reuter', 'cnn', 'western organisation', 'nfl', 'us board'], 'Automation and Employment': ['artificial intelligence', 'job automation', 'ai exposure', 'generative ai', 'coding', 'website creation', 'job losse', 'productivity', 'gdp growth', 'labor market', 'job creation'], 'machine learning': ['chatgpt', 'gpt-4'], 'large-language model': [], 'Geographic Information Systems': ['ordnance survey', 'electronic mapping', 'geographic information', 'knowledge economy', 'locations strategy', 'transformational government', 'crime hotspot', 'technology strategy', 'map update'], 'Encryption and Data Protection': ['data privacy', 'confidential', 'pgp', 'encryption'], 'Technology Procurement': ['technology', 'it transformation', 'software purchasing', 'private consultancy', 'technology strategy', 'contract procurement'], 'Gender Identity': ['transgender issue', 'gender identity', 'gid', 'nh', 'transgender', 'referral', 'medical treatment', 'keira bell', 'court case', 'gillick competence', 'trans right', 'healthcare', 'hilary cass', 'service pressure', 'regional hub', 'hormone treatment', 'research programme', 'ethical concern', 'gender non-conformity', 'treatment access', 'waiting list'], 'Religious Education': ['religious education', 'religious school', 'imam hatip', 'state education', 'islamic school', 'islam in education'], 'Socialization and Independence': ['diversity'], 'Transgender Rights': ['transgender issue', 'transgender right', 'transgender youth'], 'Public Service': [], 'Political Funding': ['oil magnate', 'political funding', 'tim dunn', 'farris wilk', 'conservative policy', 'election donation', 'state influence', 'education issue', 'private schooling', 'christian schooling', 'state legislature', 'gop', 'legislative victory', 'sports bill', 'state contribution', 'national politic', 'ted cruz', 'donald trump', 'transgender youth', 'us-mexican border', 'coronavirus restriction', 'campaign influence', 'conservative cause', 'prime minister', 'funding'], 'Renewable Energy': ['renewable energy'], 'Climate Debt': ['climate debt'], 'Carbon Tax': ['carbon tax'], 'Carbon Footprint': [], 'Sustainable Fashion': [], 'Green Technologies': [], 'us worker': [], 'ai adoption': [], 'goldman sach': [], 'white-collar': [], 'manual labor': [], 'administrative': [], 'lawyer': [], 'construction': [], 'personal computer': [], 'labor saving': [], 'electric motor': [], 'chatbot': [], 'Freedom of Information': ['freedom of information'], 'Regimental Life': ['regimental life'], 'Royal Family': ['royal family'], 'British Society': ['british society'], 'Litter Strategy': ['litter strategy'], 'Beekeeping': ['beekeeping'], 'Guardian Teach': ['guardianteach'], 'Tone': ['tone'], 'International Actor': ['international actor'], 'Exploration': ['exploration'], 'Legitimiser': [], 'Laboratory': ['laboratory'], 'Experiment': ['experiment'], 'Fieldwork': ['fieldwork'], 'Social Media': ['twitter'], 'Protest': ['protest'], 'Education': ['course update', 'scotland education', 'child development', 'nurserie', 'socialisation', 'independence', 'formal education', 'early education', 'play-orientated work', 'parent perspective', 'work pressure', 'learning enthusiasm', 'social skill', 'education structure', 'formal testing', 'child happiness', 'life choice', "child's view", 'friendship', 'summer-born', 'swedish education', 'hungarian education', 'readiness', 'play importance'], 'Politician': ['ross greer', 'politician'], 'Climate Crisis': ['naomi klein', 'climate crisis'], 'Decolonization': ['decolonization', 'imperialism', 'historical perspective', 'colonial route', 'cultural representation', 'ethical bias', 'controversy', 'heritage'], 'Fake News': ['fake news', 'alternative fact'], 'Immigration': ['immigration', 'detainee', 'u.s. immigration enforcement'], 'Government': ['intergovernmental', 'q1 2017', 'revenue'], 'Climate Change': ['kyoto protocol', 'emissions trading', 'reduction target', 'cdm'], 'Green Development': ['green development', 'trade'], 'Price': ['price']}


    def extract_dict_key(d):

            keys = {}
            for key, value in d.items():
                keys[key]=0
                if isinstance(value, dict):
                    keys.update(extract_dict_key(value))

            return keys
    print(len(extract_dict_key(data_structure)))
    def find_parent_keys(target_key, data_structure, current_path=[]):
        """


        :param target_key: input a key name, return its all parent nodes in a list
        :param data_structure:
        :param current_path:
        :return:
        """
        if target_key in data_structure:
            return current_path
        for key, value in data_structure.items():
            if isinstance(value, dict):
                path = find_parent_keys(target_key, value, current_path + [key])
                if path is not None:
                    return path
        return None
    # print(find_parent_keys("Social Impact",data_structure))
    def dict_analyse():

      labels_list = []
      for i in merged_dict:
        for ii in merged_dict[i]:
          if ii not in labels_list:
            labels_list.append(ii)

      print(len(labels_list))

    def have_common_elements(list2, list1):
      lowercase_list = [item.lower() for item in list2]
      # for ii in list2:
      for i in list1:
        if isinstance(i,list):
          for iii in i:
            if iii.lower().replace("#", "") in lowercase_list:
              return True
        else:
          if i.lower().replace("#","") in lowercase_list:
            return True
      for i in list1:
        if isinstance(i, list):
          for iii in i:
            if iii.lower().replace("#", "").replace(" ","") in lowercase_list:
              return True
        else:
          if i.lower().replace("#", "").replace(" ","") in lowercase_list:
            return True
        # return bool(set(list1) & set(list2))
    def map_label(ori_label,dict_):

      result_labels=[]
      for item in dict_:
        if have_common_elements(dict_[item],ori_label):
          result_labels.append(item)
      return result_labels
    def label_list_2_mapped_list(file_path):
      import json
      content_list=[]

      file_name_str=file_path+".jsonl"
      # file_name_str=r"C:\Users\Morning\Desktop\hiwi\heart\paper\output_labels_list.jsonl"

      with open("%s_hierarchy_labels.jsonl" % file_path,
                'w',
                encoding='utf-8') as f:
        pass
      with open(file_name_str, 'r',
                encoding='utf-8') as file:
        # 遍历文件中的每一行
        for line in file:
          # 解析每一行的JSON内容
          json_obj = json.loads(line)

          # 检查'content'键是否在JSON对象中
          if 'label_list' in json_obj:
            # 将content键的值附加到列表中
            mapped_labels=map_label(json_obj['label_list'],merged_dict)
            json_obj['mapped_labels']=mapped_labels



            with open("%s_hierarchy_labels.jsonl" % file_path,
                        'a',
                        encoding='utf-8') as f:
                json_str = json.dumps(json_obj)
                f.write(json_str + '\n')
          content_list.append(json_obj)
      print(len(content_list))
      return_label_analyse(file_path)
    def count_elements(lst):
      """
      This function takes a list as input and returns a dictionary.
      The dictionary's keys are the unique elements from the list,
      and the values are the count of occurrences of each element.
      """
      count_dict = {}
      for element in lst:
        if element in count_dict:
          count_dict[element] += 1
        else:
          count_dict[element] = 1
      return count_dict

    def return_label_analyse(file_path):


      import json

      # merged_dict = merge_dictionaries([hier, hier4, hier3, hier2])
      content_list=[]

      with open("%s_hierarchy_labels.jsonl" % file_path, 'r', encoding='utf-8') as file:
        parent_node_sum=[]
        for line in file:
              # 解析每一行的JSON内容
              json_obj = json.loads(line)
              parent_node_each_line = set()
              # 检查'content'键是否在JSON对象中
              if 'mapped_labels' in json_obj:
                # 将content键的值附加到列表中

                    content_list.extend((json_obj['mapped_labels']))
                    for label_ in json_obj['mapped_labels']:
                        # print(label_)
                        parent_node_list= find_parent_keys(label_,data_structure)
                        # print(parent_node_list)
                        if parent_node_list!=None:
                            for parent_ in parent_node_list:
                                    parent_node_each_line.add(parent_)
                        else:
                            pass
                            # print(label_,parent_node_list)

              parent_node_sum.extend(parent_node_each_line)

      num_dict=count_elements(content_list)#最底层的数据字典
      higher_level_node_num=count_elements(parent_node_sum)
      # print(merged_dict)
      print(len(content_list))
      all_keys=extract_dict_key(data_structure)

      for i in num_dict:

            update_value(all_keys,i,num_dict[i])
      for i in higher_level_node_num:
          update_value(all_keys, i, higher_level_node_num[i])
      print(all_keys)
      print(len(all_keys))

      from draw_pic import draw_pic_func
      draw_pic_func(data_structure,all_keys)
    def update_value(dictionary, key_to_update, new_value):
      """
      This function updates the value of a given key in a nested dictionary.

      :param dictionary: The nested dictionary to update.
      :param key_to_update: The key whose value needs to be updated.
      :param new_value: The new value to set for the key.
      :return: None. The dictionary is updated in place.
      """
      for key, value in dictionary.items():
        if isinstance(value, dict):
          # If the value is a dictionary, recurse.
          update_value(value, key_to_update, new_value)
        elif key == key_to_update:
          # If the key matches the key to update, update the value.
          dictionary[key] = new_value
          return


    # read_jsonl()
    # dict_analyse()
    label_list_2_mapped_list(file_path.replace(".jsonl",""))
