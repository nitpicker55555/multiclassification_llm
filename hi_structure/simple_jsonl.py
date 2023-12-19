import json
def jsonl_read(name):
    json_list=[]
    with open(name, 'r') as file:
        for line in file:
            json_line = json.loads(line)
            json_list.append(json_line)
    return json_list
