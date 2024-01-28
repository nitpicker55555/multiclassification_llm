import os
import json
from tqdm import tqdm
def calculate_and_draw_func(data_structure,merged_dict,file_path,final_mapping_dict):
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
    print(len(extract_dict_key(data_structure)),"len(extract_dict_key(data_structure))")
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

    def map_label(processed_labels,dict_,discard_word):

          result_labels=[]
          ori_label=[]
          for item in processed_labels:
              if item in final_mapping_dict:
                  ori_label.append(final_mapping_dict[item] )
                  discard_word[0]+=1
              else:
                  discard_word[1] += 1
                  discard_word[2].append(item)
          # ori_label=[final_mapping_dict[item] for item in processed_labels if item in final_mapping_dict]
          # print(len(ori_label),"ori")
          for item in dict_:
            if have_common_elements(dict_[item],ori_label):
              result_labels.append(item)
          return result_labels,discard_word
    def label_list_2_mapped_list(file_path):
        try:
            with open("%s_hierarchy_labels.jsonl" % file_path,
                      'w',
                      encoding='utf-8') as f:
                pass
        except:
            pass
        discard_word=[0,0,[]]
        mapped_label_list=[]
        print(file_path,"label_list_2_mapped_list")
        if "merged" in file_path:
            file_name_str = file_path + ".jsonl"
        else:
            file_name_str=file_path+"_labels.jsonl"
        # file_name_str=r"C:\Users\Morning\Desktop\hiwi\heart\paper\output_labels_list.jsonl"

        with open(file_name_str, 'r',
                  encoding='utf-8') as file:
            # 遍历文件中的每一行
            for line in tqdm(file,desc="map_label"):
                # 解析每一行的JSON内容
                json_obj = json.loads(line)

                # 检查'content'键是否在JSON对象中
                if 'label_list' in json_obj:
                    # 将content键的值附加到列表中
                    mapped_labels,discard_word = map_label(json_obj['label_list'], merged_dict,discard_word)
                    json_obj['mapped_labels'] = mapped_labels

                    with open("%s_hierarchy_labels.jsonl" % file_path,
                              'a',
                              encoding='utf-8') as f:
                        json_str = json.dumps(json_obj)
                        f.write(json_str + '\n')
                mapped_label_list.append(json_obj)
        print(len(mapped_label_list),"sum value")
        # print(discard_word,"discard_word")
        all_num_keys = return_label_analyse(mapped_label_list)
        return all_num_keys
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

    def return_label_analyse(mapped_label_list):




          # merged_dict = merge_dictionaries([hier, hier4, hier3, hier2])
            content_list=[]

          # with open("%s_hierarchy_labels.jsonl" % file_path, 'r', encoding='utf-8') as file:
            parent_node_sum=[]
            for line in mapped_label_list:
                  # 解析每一行的JSON内容
                  json_obj = line
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
            all_num_keys=extract_dict_key(data_structure)

            for i in num_dict:

                update_value(all_num_keys,i,num_dict[i])
            for i in higher_level_node_num:
              update_value(all_num_keys, i, higher_level_node_num[i])
            # print("num_labels_dict: ",all_num_keys)
            print(len(all_num_keys))
            return all_num_keys

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
    return  label_list_2_mapped_list(file_path.replace(".jsonl","").replace(".xlsx",""))
def convert_lists_to_sets(d):
    """
    Recursively convert all lists in a nested dictionary to sets.
    """
    for key, value in d.items():
        if isinstance(value, list):
            d[key] = set(value)
        elif isinstance(value, dict):
            convert_lists_to_sets(value)

# from ddd_map_words_to_dicts import map_words_2_dicts
# from ccc_get_structure import get_structure
# from bbb_clean_and_alignment import get_clean_word
# from bbb_clean_and_alignment import get_cluster
# from bbb_clean_and_alignment import make_alignment
# from aaa_model_set_label import main_model
def convert_lists_to_sets_in_dict(nested_dict):
    for key, value in nested_dict.items():
        if isinstance(value, list):
            nested_dict[key] = set(value)
        elif isinstance(value, dict):
            convert_lists_to_sets_in_dict(value)
    return nested_dict
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Example Script with Named Arguments')


    parser.add_argument('--file_path', type=str, help='file_path')
    args = parser.parse_args()
    file_path=args.file_path
    file_name = os.path.basename(args.file_path)
# twitter_files\2018-1-1_2018-12-31_without_profile_labels.jsonl
    #C:\Users\Morning\Desktop\hiwi\heart\paper\hi_structure\tem_file\tem_file\mapped_dicts_2017-1-1_2017-12-31_without_profile_labels.jsonl
    json_structure_name=r'tem_file\json_structure_'+file_name
    mapped_dicts_name=r'tem_file\mapped_dicts_'+file_name
    twitter_original_name=file_path.replace("_labels.jsonl",".jsonl")
    final_mapping_dict=r'tem_file\final_mapping_dict'+file_name
    # from simple_jsonl import jsonl_read
    with open(json_structure_name,'r') as file:
        json_str=file.read()
    json_structure=json.loads(json_str)
    json_structure=convert_lists_to_sets_in_dict(json_structure)
    with open(mapped_dicts_name,'r') as file:
        json_str=file.read()
    mapped_dicts=json.loads(json_str)
    with open(final_mapping_dict,'r') as file:
        json_str=file.read()
    final_mapping_dict=json.loads(json_str)
    all_num_keys=calculate_and_draw_func(json_structure,mapped_dicts,twitter_original_name,final_mapping_dict)
    # from draw_pic import draw_pic_func
    with open(r"tem_file\all_num_key"+file_name,
              'w',
              encoding='utf-8') as f:
        json_str = json.dumps(all_num_keys)
        f.write(json_str + '\n')
    from draw_pic_sunburst import draw_pic

    draw_pic(json_structure,all_num_keys ,file_name.replace(".jsonl",""))
    # draw_pic_func(json_structure, all_num_keys,num_str)

# file_name=r'sum_all_labels.jsonl'

# json_structure=get_structure(file_name)
#
# convert_lists_to_sets(json_structure)
# print(json_structure)
# calculate_and_draw_func(json_structure,map_words_2_dicts(json_structure,file_name),file_name)

# json_structure={'Privacy': {'Data Breach': {'data exposure', 'data breaches', 'GPS privacy breach', 'data breach', 'data leak'}, 'Personal Information': {'email addresses', 'name', 'passport numbers', 'home addresses', 'phone numbers'}, 'Concerns': {'privacy policy', 'privacy concerns', 'privacy issues', 'privacy breaches', 'user privacy'}, 'Incidents': {'security breach', 'incident', 'privacy breach', 'Unauthorized GPS tracking', 'location data exposure'}}, 'Technology': {'Navigation': {'satellite navigation systems', 'Global Positioning System', 'GPS', 'Navigation system', 'navigation system'}, 'Security': {'security flaw', 'encryption', 'data security', 'cybersecurity', 'vulnerability'}, 'Devices': {'Bluetooth technology', 'device', 'smartphones', 'GPS devices', 'tracking devices'}}, 'Information': {'Types': {'sensitive information', 'location data', 'personal data', 'customer data', 'user data'}, 'Leaks': {'data leaks', 'unauthorized access', 'mishandle', 'security lapse', 'stolen data'}}, 'Legal': {'Actions': {'penalty', 'investigation', 'settlement', 'lawsuit', 'violation'}, 'Regulations': {'General Data Protection Regulation', 'law', 'privacy rights', 'data protection laws'}}, 'Companies': {'Tech Giants': {'Apple', 'Facebook', 'TikTok', 'Google', 'Meta'}, 'Services': {'NHS', 'Uber', 'Grindr', 'Strava', 'Aarogya Setu'}}, 'Government': {'Entities': {'authority', 'European Commission', 'Pentagon', 'law enforcement', 'government'}, 'Issues': {'privacy settings', 'law', 'regulation', 'policy', 'data sharing'}}, 'Incidents': {'System Failures': {'system failure', 'GPS malfunction', 'malfunction', 'Navigation system failure', 'error'}, 'Breaches': {'data exposure', 'GPS privacy breach', 'security breach', 'data breach', 'privacy breach'}}, 'Geopolitical': {'Countries': {'India', 'United States', 'UK', 'China', 'Russia'}, 'Conflicts': {'Ukraine', 'military', 'Pentagon', 'military bases', 'Afghanistan'}}}
# merged_dict={'data exposure': ['spreadsheet', 'real-time location data', 'data exposure'], 'data breaches': ['data breaches', 'data breach', 'data leak', 'data leaks', 'data breaches', 'data security', 'misuse', 'unauthorized access', 'Pegasus spyware', 'security breach', 'security lapse', 'data exposure', 'fraud', 'data breaches'], 'GPS privacy breach': [], 'data breach': ['data breach', 'breach', 'data breach', 'data breaches', 'data leak', 'data leaks', 'data security', 'misuse', 'unauthorized access'], 'data leak': ['data leak', 'data breach', 'data breaches', 'data leak', 'data leaks', 'data security', 'misuse', 'unauthorized access'], 'email addresses': ['email addresses', 'email address'], 'name': ['name', 'names'], 'passport numbers': ['passport numbers'], 'home addresses': ['home addresses'], 'phone numbers': ['phone numbers', 'phone number'], 'privacy policy': ['privacy policy', 'statement', 'privacy policies'], 'privacy concerns': ['privacy', 'concern', 'privacy concerns', 'privacy issues', 'privacy breaches', 'GPS privacy breach concerns'], 'privacy issues': ['privacy concerns', 'privacy issues', 'privacy breaches'], 'privacy breaches': ['privacy concerns', 'privacy issues', 'privacy breaches'], 'user privacy': ['user privacy'], 'security breach': ['security breach'], 'incident': ['incident', 'incidents'], 'privacy breach': ['privacy breach'], 'Unauthorized GPS tracking': ['Unauthorized GPS tracking'], 'location data exposure': ['Location data exposure', 'location data exposure', 'real-time location data', 'location information'], 'satellite navigation systems': ['navigation system', 'Navigation system', 'navigation system', 'Navigation system', 'Navigation system data leak', 'satellite navigation systems', 'satellite navigation system'], 'Global Positioning System': ['GPS', 'GPS', 'Global Positioning System', 'GPS', 'GPS', 'GPS', 'GPS coordinates'], 'GPS': ['GPS', 'GPS', 'Global Positioning System', 'GPS', 'GPS signals', 'malfunction', 'GPS', 'GPS', 'GPS interference', 'GPS systems', 'GPS', 'GPS coordinates'], 'Navigation system': ['Navigation system', 'navigation system', 'Navigation system', 'navigation system', 'Navigation system', 'Navigation system data leak', 'navigation system errors', 'system failure', 'navigation systems', 'Navigation system', 'Navigation system', 'navigation system', 'Navigation system failure', 'Navigation system'], 'navigation system': ['Navigation system', 'navigation system', 'Navigation system', 'navigation system', 'Navigation system', 'Navigation system data leak', 'navigation system errors', 'system failure', 'navigation systems', 'navigation system', 'Navigation system', 'navigation system', 'navigation system'], 'security flaw': ['security flaw'], 'encryption': ['encryption'], 'data security': ['data security'], 'cybersecurity': ['cybersecurity'], 'vulnerability': ['vulnerability'], 'Bluetooth technology': ['Bluetooth technology', 'Bluetooth signals'], 'device': ['device', 'Android app', 'computer'], 'smartphones': ['smartphones'], 'GPS devices': ['tracking devices'], 'tracking devices': ['tracking devices'], 'sensitive information': ['sensitive information', 'driver license numbers', 'sensitive personal information', 'Social Security numbers', 'personally identifiable information', 'passenger information', 'sensitive medical information', 'payment card information', 'patient records'], 'location data': ['location data', 'location data', 'real-time location data', 'location information', 'user location data', 'GPS locations'], 'personal data': ['personal data', 'personal information'], 'customer data': ['customer data'], 'user data': ['user', 'user data', 'user accounts', 'usernames', 'user profiles'], 'data leaks': ['data leaks', 'data breach', 'data breaches', 'data leak', 'data leaks', 'data security', 'misuse', 'unauthorized access', 'data leaks'], 'unauthorized access': ['data breach', 'data breaches', 'data leak', 'data leaks', 'data security', 'misuse', 'unauthorized access'], 'mishandle': ['mishandle'], 'security lapse': ['security lapse', 'lapse'], 'stolen data': ['stolen data'], 'penalty': ['penalty'], 'investigation': ['investigation', 'investigate'], 'settlement': ['settlement'], 'lawsuit': ['lawsuit'], 'violation': ['violation'], 'General Data Protection Regulation': ['General Data Protection Regulation'], 'law': ['law'], 'privacy rights': [], 'data protection laws': ['data protection laws', 'data protection regulations'], 'Apple': ['Apple'], 'Facebook': ['Facebook', 'Cambridge Analytica'], 'TikTok': ['TikTok'], 'Google': ['Google'], 'Meta': ['Meta'], 'NHS': ['NHS'], 'Uber': ['Uber'], 'Grindr': ['Grindr'], 'Strava': ['Strava'], 'Aarogya Setu': ['Aarogya Setu'], 'authority': ['authority', 'attorney general', 'government', 'European Commission', 'federal government', 'government departments'], 'European Commission': ['European Commission'], 'Pentagon': ['Pentagon'], 'law enforcement': ['law enforcement'], 'government': ['government', 'government', 'government departments', 'federal government'], 'privacy settings': ['privacy settings'], 'regulation': ['regulation'], 'policy': ['policy'], 'data sharing': ['data sharing'], 'system failure': ['system failure'], 'GPS malfunction': ['malfunction', 'GPS malfunction', 'GPS malfunction', 'Navigation system failure'], 'malfunction': ['malfunction', 'GPS malfunction', 'Navigation system failure'], 'Navigation system failure': ['Navigation system failure', 'Navigation system error incidents', 'system failure', 'Navigation system failure'], 'error': ['error'], 'India': ['India', 'India', 'Aarogya Setu'], 'United States': ['United States', 'US', 'U.S.', 'United States'], 'UK': ['UK', 'UK'], 'China': ['China', 'China'], 'Russia': ['Russia', 'Russia'], 'Ukraine': ['Ukraine', 'Ukraine'], 'military': ['military', 'military personnel', 'Chinese military', 'military', 'military bases'], 'military bases': ['military bases', 'military bases'], 'Afghanistan': ['Afghanistan'], 'navigation system errors': ['navigation system errors'], 'GPS signals': ['GPS signals'], 'topic': [], 'case': [], 'accuracy': [], 'monitor': [], 'police': [], 'apps': [], 'notification': [], 'map': [], 'software': [], 'hospital': [], 'full names': [], 'organization': [], 'IP addresses': [], 'internet': [], 'complaint': [], 'interest': [], 'attacker': [], 'spyware': [], 'healthcare system': [], 'theft': [], 'plan': [], 'backup systems': [], 'communication': [], 'train': [], 'response': [], 'payment': [], 'safety concerns': [], 'aircraft': [], 'collision': [], 'investigator': [], 'receiver': [], 'jam': [], 'reliance': [], 'challenge': [], 'security concerns': [], 'impact': [], 'warning': [], 'warn': [], 'difficulty': [], 'European Union': [], 'adoption': [], 'dependence': [], 'market': [], 'Norway': [], 'target': [], 'method': [], 'drone': [], 'article': ['article', 'news article'], 'firm': [], 'client': [], 'Office of Personnel Management': [], 'sensitive personal information': [], 'dating app': [], 'vehicle owners': [], 'effort': [], 'dataset': [], 'city': [], 'microphone': [], 'Europe': [], 'fitness tracking app': [], 'photo': [], 'CEO': [], 'age': [], 'statement': [], 'GPS privacy breach concerns': [], 'member': [], 'worldwide': [], 'citizen': [], 'space': [], 'third parties': [], 'news article': [], 'patient data': [], 'safeguard': [], 'access tokens': [], 'precise location data': [], 'Pegasus': [], 'government agencies': [], 'GPS tracking devices': [], 'telephone numbers': [], 'call': [], 'compliance': [], 'network': [], 'journalist': [], 'Android users': [], 'location-related information': [], 'geolocation': [], 'contact': [], 'operation': [], 'file': [], 'Toyota': [], 'Japan': [], 'Location data': [], 'mobile devices': [], 'TechCrunch': [], 'Tesla': [], 'Germany': [], 'number': [], 'tech companies': [], 'consumer': [], 'whistleblower': [], 'user information': [], 'Amazon Web Services': [], 'birthdates': [], 'release': [], 'department': [], 'search': [], 'location history': [], 'transparency': [], 'resident': [], 'security flaws': [], 'device settings': [], 'profit': [], 'AirTags': [], 'privacy experts': [], 'privacy laws': [], 'Elon Musk': [], 'public': [], 'customer information': [], 'postal addresses': [], 'Americans': [], 'candidate': [], 'Medicare numbers': [], 'EU': [], 'storage': [], 'social security numbers': [], 'government clients': [], 'British Airways': [], 'Information Commissioner’s Office': [], 'ICO': [], 'apology': [], 'law firm': [], 'parent': [], 'ransom': [], 'security issues': [], 'concept': [], 'image': [], 'cost': [], 'safety measures': [], 'navigation system error incidents': [], 'inquiry': [], 'spacecraft': [], 'injury': [], 'importance': [], 'brake': [], 'Hawaii': [], 'eLoran': [], 'terminal': [], 'computer failure': [], 'airline': [], 'Nats': [], 'Kazakhstan': [], 'airport': [], 'activity': [], 'trial': [], 'position': [], 'safety incidents': [], 'security risks': [], 'smartwatches': [], 'manufacturer': [], 'GPS services': [], 'sensor': [], 'feature': [], 'dangerous situations': [], 'cost overruns': [], 'factor': [], 'alternative': [], 'competition': [], 'GPS satellite': [], 'ban': [], 'supply chain': [], 'Spain': [], 'privacy policies': [], 'ride': [], 'attorney general': ['attorney general'], 'stalker': [], 'demand': [], 'health': ['health'], 'user location data': ['user location data'], 'delivery addresses': [], 'subset of users': [], 'payment card information': ['payment card information'], 'phone number': ['phone number'], 'email address': ['email address'], 'example': [], 'centralized database': [], 'government employees': [], 'family members': [], 'privacy invasion': [], 'spy': [], 'exercise': [], 'malicious intent': [], 'agriculture': [], 'Chinese military': ['Chinese military'], 'influence': [], 'national security': ['national security'], 'privacy protection': [], 'proximity': [], 'federal government': ['federal government'], 'mandatory use': [], 'government departments': ['government departments'], 'COVID-19 pandemic': [], 'European users': [], 'mission': [], 'GPS coordinates': ['GPS coordinates'], 'plaintext passwords': [], 'privacy risk': [], 'authorization': [], 'data privacy breaches': [], 'GPS locations': ['GPS locations'], 'lapse': ['lapse'], 'user profiles': ['user profiles'], 'association': [], 'insight': [], 'data protection regulations': ['data protection regulations'], 'legislative changes': [], 'warrant': [], 'patient records': ['patient records'], 'thousand': [], 'history': [], 'photos': [], 'Israeli company': []}
# calculate_and_draw_func(json_structure,merged_dict,file_name)