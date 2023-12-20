import json
num_str="17"
def convert_lists_to_sets_in_dict(nested_dict):
    for key, value in nested_dict.items():
        if isinstance(value, list):
            nested_dict[key] = set(value)
        elif isinstance(value, dict):
            convert_lists_to_sets_in_dict(value)
    return nested_dict
json_structure_name = r'tem_file\json_structure_20%s-1-1_20%s-12-31_without_profile_labels.jsonl' % (num_str, num_str)
mapped_dicts_name = r'tem_file\mapped_dicts_20%s-1-1_20%s-12-31_without_profile_labels.jsonl' % (num_str, num_str)
twitter_original_name = r'twitter_files\20%s-1-1_20%s-12-31_without_profile.jsonl' % (num_str, num_str)
final_mapping_dict = r'tem_file\final_mapping_dict20%s-1-1_20%s-12-31_without_profile_labels.jsonl' % (num_str, num_str)
# from simple_jsonl import jsonl_read
with open(json_structure_name, 'r') as file:
    json_str = file.read()
json_structure = json.loads(json_str)
json_structure = convert_lists_to_sets_in_dict(json_structure)



value={"root":18810,"Technology & Computing": 16842, "Artificial Intelligence": 16817, "Core Concepts": 3428, "nearest neighbor algorithm": 170, "neurocontroller": 172, "brain-computer interface": 2174, "algorithmic algorithm": 1350, "neutrino-neural network": 69, "biological computing": 1900, "genetic algorithm": 146, "machine learning": 1483, "Applications": 2344, "natural language processing": 61, "data mining": 2116, "image recognition": 115, "fuzzy set theory": 123, "Ethics & Policy": 16742, "artificial intelligence ethic": 16699, "policy development": 546, "ethical guideline": 16730, "Computer Science": 4394, "Software Development": 1083, "cloud computing": 253, "data model development": 680, "intrusion detection": 187, "fault-tolerance": 55, "Data Management": 4078, "data processing": 4003, "data warehouse": 8, "data visualization": 282, "database management": 1777, "Emerging Technologies": 621, "3-D printing technology": 71, "neuromuscular engineering": 16, "sensor technology": 448, "biomarkeromic": 100, "Cybersecurity": 1412, "Security Measures": 690, "cyber security": 423, "intrusion detection system": 163, "data safety": 434, "Privacy": 276, "intellectual property": 149, "data privacy": 151, "Ethical Considerations": 16797, "privacy ethics": 55, "data democratizing": 797, "Ethics & Society": 16851, "Technology Ethics": 16733, "technology and science ethics": 16731, "biomedical ethics": 71, "ergonomic design ethic": 2852, "Social Responsibility": 16753, "ethical and social responsibility": 16753, "suicide prevention": 2846, "human rights": 541, "Social Impact": 4874, "Computing & Society": 638, "health care administration": 502, "social science computing": 137, "Public Policy": 4778, "public interest": 4706, "social justice": 563, "Legal & Policy": 1340, "Regulatory Aspects": 1340, "legal issues": 514, "regulation": 778, "law": 618, "Intellectual Property": 166, "patent policy": 127, "copyright law": 166, "Science & Research": 4672, "Biological Sciences": 809, "Genetics & Genomics": 538, "genomics": 125, "molecular biology": 514, "Cellular & Molecular": 575, "biochemistry": 249, "cell biology": 166, "biomedical engineering": 354, "Medical Sciences": 2404, "Research & Development": 2253, "cancer research": 293, "medical research": 2025, "disease prevention": 674, "Clinical Applications": 566, "neonatology": 89, "medical genetics": 97, "neurology": 432, "Data Science": 2740, "Analytics": 2705, "data analytics": 868, "predictive analytics": 319, "big data": 2376, "Statistical Methods": 2024, "regression analysis": 68, "statistical analysis": 2004, "Business & Industry": 2578, "Industry Sectors": 1512, "Finance & Insurance": 301, "insurtech": 282, "fintech": 264, "Telecommunications & Technology": 1356, "automotive industry": 102, "telecommunications": 1261, "Management & Strategy": 811, "Human Resources": 204, "human resource management": 204, "Strategic Planning": 672, "business strategy": 632, "corporate governance": 198, "Marketing & Media": 1199, "Digital Marketing": 521, "digital marketing": 403, "content marketing": 130, "Media": 839, "media and journalism": 718, "public relations": 215, "Education & Learning": 3487, "Academic Studies": 2208, "Humanities & Social Sciences": 849, "history": 65, "philosophy of science": 460, "psychology": 389, "Scientific & Technical": 1434, "technology education": 166, "mathematics": 1282, "Professional Development": 1609, "Skills Training": 894, "workforce training": 161, "career development": 894, "Educational Methods": 1246, "teaching methodologies": 344, "skill acquisition": 1228, "Educational Technology": 408, "E-Learning": 313, "edtech": 305, "e-learning": 52, "Instructional Tools": 353, "distance education": 47, "educational software": 327}


# print(elements)
# print(parents)
from draw_pic_sunburst import draw_pic
draw_pic(json_structure,value,"12")