aa={
        'Decision and Control': {
            'AI decision-making flaw': 52,
            'Control and execution issues': 43,
            'Path planning problem': 35
        }}

def sum_dict(dict_sample,sum_value=0):

    for key, value in dict_sample.items():
        if isinstance(list(value.values())[0], dict):
            sum_value+=sum_dict(dict_sample[key],sum_value)
        else:

            sum_value+=sum(value.values())
    return sum_value
print(sum_dict(aa))
