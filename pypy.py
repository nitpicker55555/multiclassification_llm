dict_length = {'Traffic Accidents':{
    'Technical Issues': {
        'Decision and Control': {
            'AI decision-making flaw': 52,
            'Control and execution issues': 43,
            'Path planning problem': 35
        },
        'Hardware and Integration': {
            'Sensor or data input error': 27,
            'System integration and hardware issues': 2,
            'Hardware or software failure': 9
        },
        'Data and Processing': {
            'Data processing error': 14,
            'Training data and validation issues': 2
        },
        'System Robustness and Fault Tolerance': {
            'System robustness and fault tolerance issues': 46
        }
    },
    'Human-Computer Interaction Issues': {
        'Human-computer interaction problem': 16,
        'Driver distraction due to over-reliance on technology': 34,
        'Human factors other than the driver': 3,
        'Insufficient feedback mechanism': 11,
        'Communication and interaction issues': 8,
        'Transparency and interpretability issues': 2
    },
    'Safety Issues': {
        'Causing safety threats to others other than passengers': 34,
        'Emergency response issues': 30,
        'Threat to passenger safety': 37
    },
    'Data Issues': {
        'Inaccurate or incomplete data': 18
    },
    'Human Operational Issues': {
        'Driver operation problem': 10
    }
},'Discrimination':{'Nationality discrimination': 2,
    'Racial discrimination': 8,
    'Sex discrimination': 1}}

"""
1. 输出每一层的数量列表
2. 
"""
# first_dict = {}
# second_dict={}
# third_dict={}
# for key,value in dict_length.items():
#     if isinstance(list(value.values())[0],dict):
#         # print(key)
#         third_dict=dict_length[key]
#         second_dict[key]={}
#         first_dict[key]=0
#         for key2,value2 in value.items():
#             # print(value2)
#             first_dict[key] +=sum(value2.values())
#             second_dict[key][key2]=sum(value2.values())
#
#
#         # print(first_dict)
#     else:
#         first_dict[key] = sum(value.values())
# print(first_dict)
# print(second_dict)
# print(third_dict)
"""
{'Technical Issues': 230, 'Human-Computer Interaction Issues': 74, 'Safety Issues': 101, 'Data Issues': 18, 'Human Operational Issues': 10}
{'Technical Issues': {'Decision and Control': 130, 'Hardware and Integration': 38, 'Data and Processing': 16, 'System Robustness and Fault Tolerance': 46}}
{'Decision and Control': {'AI decision-making flaw': 52, 'Control and execution issues': 43, 'Path planning problem': 35}, 'Hardware and Integration': {'Sensor or data input error': 27, 'System integration and hardware issues': 2, 'Hardware or software failure': 9}, 'Data and Processing': {'Data processing error': 14, 'Training data and validation issues': 2}, 'System Robustness and Fault Tolerance': {'System robustness and fault tolerance issues': 46}}

"""
first_dict = {}
second_dict={}
third_dict={}

result_list={}
def sum_dict(dict_sample,sum_value=0):
    # print(dict_sample)
    for key, value in dict_sample.items():
        if isinstance(list(value.values())[0], dict):
            sum_value+=sum_dict(dict_sample[key],sum_value)
        else:

            sum_value+=sum(value.values())
    return sum_value

def check_dict(depth,result_list,dict_sample,parent="Root"):
    merged_dict = {}
    depth += 1
    if depth==2:
        print(depth)
    if depth not in result_list:
        result_list[depth] = {}
    for key, value in dict_sample.items():
        if isinstance((value), dict):
            merged_dict[key] = sum_dict({key:dict_sample[key]})

            check_dict(depth,result_list,dict_sample[key],key)
        else:
            merged_dict[key]=dict_sample[key]

    result_list[depth].update({parent:merged_dict})

    return result_list
result=check_dict(0,result_list,dict_length)

print(result)
print(second_dict)
print(third_dict)
total_list=[first_dict,second_dict,third_dict]
for i in result:
    print(i,result[i])
