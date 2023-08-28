a={'Driver operation problem': 10, 'AI decision-making flaw': 52, 'Control and execution issues': 43, ' Human-computer interaction problem': 16, 'Causing safety threats to others other than passengers': 34, 'Driver distraction due to over-reliance on technology': 34, 'Emergency response issues': 30, 'Threat to passenger safety': 37, 'System robustness and fault tolerance issues': 46, 'Path planning problem': 35, 'Data processing error': 14, 'Insufficient feedback mechanism': 11, 'Inaccurate or incomplete data': 18, 'Human factors other than the driver': 3, 'Communication and interaction issues': 8, 'Sensor or data input error': 27, 'System integration and hardware issues': 2, 'Training data and validation issues': 2, 'Hardware or software failure': 9, 'Transparency and interpretability issues': 2}

autonomous_driving_issues = {
    "Technical Issues": {
        "Decision and Control": [
            "AI decision-making flaw",
            "Control and execution issues",
            "Path planning problem"
        ],
        "Hardware and Integration": [
            "Sensor or data input error",
            "System integration and hardware issues",
            "Hardware or software failure"
        ],
        "Data and Processing": [
            "Data processing error",
            "Training data and validation issues"
        ],
        "System Robustness and Fault Tolerance": [
            "System robustness and fault tolerance issues"
        ]
    },
    "Human-Computer Interaction Issues": [
        "Human-computer interaction problem",
        "Driver distraction due to over-reliance on technology",
        "Human factors other than the driver",
        "Insufficient feedback mechanism",
        "Communication and interaction issues",
        "Transparency and interpretability issues"
    ],
    "Safety Issues": [
        "Causing safety threats to others other than passengers",
        "Emergency response issues",
        "Threat to passenger safety"
    ],
    "Data Issues": [
        "Inaccurate or incomplete data"
    ],
    "Human Operational Issues": [
        "Driver operation problem"
    ]
}
autonomous_driving_child = {
    "Technical Issues": {

    },
    "Human-Computer Interaction Issues": [

    ],
    "Safety Issues": [

    ],
    "Data Issues": [

    ],
    "Human Operational Issues": [

    ]
}
second_dict={}
i=0
for key, value in autonomous_driving_issues.items():
    if isinstance(value, list):
        # print(f"{key} is a list.")
        for item_ in autonomous_driving_issues[key]:
            i += 1
            print(item_)
    else:
        # print(f"{key} is not a list.")
        for sub_key, sub_value in value.items():
            if isinstance(sub_value, list):
                # print(f"  - {sub_key} is a list.")
                for item_ in autonomous_driving_issues[key][sub_key]:
                    i += 1
                    if item_ not in a:

                        print(item_)
            else:
                pass
                # print(f"  - {sub_key} is not a list.")
print(i)
print(len(a))
def transform_nested_dict(nested_dict, reference_dict):
    for key, value in nested_dict.items():
        if isinstance(value, dict):
            transform_nested_dict(value, reference_dict)
        elif isinstance(value, list):
            new_list = []
            for item in value:
                if item in reference_dict:
                    new_list.append({item: reference_dict[item]})
                else:
                    new_list.append(item)
            nested_dict[key] = new_list
    return nested_dict

transformed_autonomous_driving_issues = transform_nested_dict(autonomous_driving_issues.copy(), a)
print(transformed_autonomous_driving_issues)
dict_list={'Technical Issues': {'Decision and Control': [{'AI decision-making flaw': ['3', '4', '5', '7', '8', '10', '13', '14', '15', '16', ' 18', '19', '20', '21', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '42', '43', '44', '46', '47', '49', '50', ' 51', '52', '53', '54', '57', '58', '59', '60', '61', '63', '64', '65', '66', '67', '68', '69', '71']}, {'Control and execution issues': ['3', '6', '7', '10', '13', '14', '15', '16', '18', '19', '21', '23', '24', '25', '26', '27', '28', '29', '30 ', '34', '35', '37', '42', '43', '44', '45', '46', '51', '52', '53', '54', '57', '58', '59', '60', '61', '63', '64', '65', '67', '68', '69', '71']}, {'Path planning problem': ['5', '7', '10', '15', '16', '18', '19', '20', '23', ' 24', '26', '29', '30', '31', '32', '33', '34', '35', '36', '42', '43', '44', '46', '51', '52', '53', '54', '57', '60', '61', '63', '64', '65', '67', ' 71']}], 'Hardware and Integration': [{'Sensor or data input error': ['8', '10', '13', '14', '15', '16', '18', '19', '20', '21', '23', '24', '25', '26', '27', '29', '30', '34', '35 ', '47', '49', '50', '58', '59', '61', '64', '66']}, {'System integration and hardware issues': ['10', '27 ']}, {'Hardware or software failure': ['21', '23', '27', '28', '37', ' 44', '58', '59', '64']}], 'Data and Processing': [{'Data processing error': ['5', '13', '20', '21', '23', '24', '27', '31', '32', '33', '58', '59', '64', '66']}, {'Training data and validation issues': ['13', '66']}], 'System Robustness and Fault Tolerance': [{'System robustness and fault tolerance issues': ['4', '5', '7', '10', '13', '14', '15', ' 16', '18', '19', '20', '21', '23', '24', '25', '26', '27', '28', '29', '30', '34', '35', '37', '42', '43', '44', '45', '46', '47', '49', '50', '51', ' 52', '53', '54', '57', '58', '59', '60', '61', '64', '65', '67', '68', '69', '71']}]}, 'Human-Computer Interaction Issues': [{'Human-computer interaction problem': ['3', '4', '5', '8', '9', '16', '24', '30', '31', '32', '33', '36', '60', '65', '66', '70']}, {'Driver distraction due to over-reliance on technology': ['4', '5', '8', '9', '14', '15', '19', '20', '24', '29', '30', '31', '32', '33', '34', '35', ' 36', '44', '46', '47', '49', '50', '51', '52', '53', '54', '57', '58', '59', '61', '63', '67', '69', '70']}, {'Human factors other than the driver': ['6', '21', '25']}, {'Insufficient feedback mechanism': ['5', '8', '9', '10', '14', '23', ' 36', '36', '60', '64', '65']}, {'Communication and interaction issues': ['7', '7', '21', '23', '24', '26', '37', '60']}, {'Transparency and interpretability issues': ['21', '66']}], 'Safety Issues': [{'Causing safety threats to others other than passengers': ['3', '4', '9', '14', '16', '19', '23', '24', '25', '27', '28', '29', '30', '31', '35', '36', '37 ', '43', '46', '47', '49', '50', '52', '53', '54', '59', '61', '63', '65', '67', '68', '69', '70', '71']}, {'Emergency response issues': ['4', '5', '6', '8', '9', ' 14', '19', '23', '24', '25', '26', '28', '29', '34', '35', '37', '47', '49', '50', '51', '52', '53', '54', '57', '61', '65', '67', '68', '69', '70']}, {'Threat to passenger safety': ['4', '5', '6', '8', '9', '15', '19', '20', '21', '26', ' 27', '28', '32', '33', '34', '42', '43', '44', '45', '47', '49', '50', '51', '52', '53', '57', '58', '59', '60', '61', '63', '66', '67', '68', '69', ' 70', '71']}], 'Data Issues': [{'Inaccurate or incomplete data': ['5', '13', '15', '16', '18', '20', '21', '27', '31', '32', '33', '34', '35', '36', '58', '59', '63', '66 ']}], 'Human Operational Issues': [{'Driver operation problem': ['3', '8', '9', '24', '25', '26', '30', '61', '63', '70']}]}
dict_length={'Technical Issues': {'Decision and Control': [{'AI decision-making flaw': 52}, {'Control and execution issues': 43}, {'Path planning problem': 35}], 'Hardware and Integration': [{'Sensor or data input error': 27}, {'System integration and hardware issues': 2}, {'Hardware or software failure': 9}], 'Data and Processing': [{'Data processing error': 14}, {'Training data and validation issues': 2}], 'System Robustness and Fault Tolerance': [{'System robustness and fault tolerance issues': 46}]}, 'Human-Computer Interaction Issues': [{'Human-computer interaction problem':16}, {'Driver distraction due to over-reliance on technology': 34}, {'Human factors other than the driver': 3}, {'Insufficient feedback mechanism': 11}, {'Communication and interaction issues': 8}, {'Transparency and interpretability issues': 2}], 'Safety Issues': [{'Causing safety threats to others other than passengers': 34}, {'Emergency response issues': 30}, {'Threat to passenger safety': 37}], 'Data Issues': [{'Inaccurate or incomplete data': 18}], 'Human Operational Issues': [{'Driver operation problem': 10}]}
def transform_nested_tree(nested_dict):
    second_child={}
    for key, value in nested_dict.items():
        if isinstance(value, dict):
            # transform_nested_dict(value, reference_dict)
            print(key)
            print("______")
            num=0
            third_child={}
            for child_key,child_value in value.items():
                total_sum = sum(int(true_value) for one_value in child_value for true_value in one_value.values())
                print(child_key,total_sum)
                num+=total_sum
                third_child[child_key]=total_sum
            print(third_child)
            second_child[key] = num
        elif isinstance(value, list):

            print(key)
            print("++++++++")
            total_sum = sum(int(true_value) for one_value in value for true_value in one_value.values())
            third_child = {k:v for one_value in value for k,v in one_value.items()}

            print(third_child)
            second_child[key]=total_sum
    print(second_child)
    return second_child
#second_child={'Technical Issues': 230, 'Human-Computer Interaction Issues': 74, 'Safety Issues': 101, 'Data Issues': 18, 'Human Operational Issues': 10}

transform_nested_tree(dict_length)