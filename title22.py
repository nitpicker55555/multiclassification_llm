import json
import re

text = """Based on the provided information, it is not clear whether there is a privacy violation in the news. Privacy violations typically involve the unauthorized or inappropriate disclosure of personal information. The information provided in the news article does not explicitly mention a privacy violation. Therefore, the answer is:
asd
Based on the information provided in the news, there doesn't appear to be any mention or indication of privacy violation. The incident revolves around an accident with a robot and bear repellent at an Amazon warehouse. 

Therefore, the appropriate JSON response would be:

```json
{
    "privacy violation": "False"
}

```
asd
"""


def extract_dict(text,key_str="privacy violation"):
    text=text.lower()
    if key_str!="multikey":
        match = re.search(r'{\s*"%s":\s*(true|false)\s*}'%key_str, text)
        json_str = match.group(0) if match else None
        if json_str:
            dictionary = json.loads(json_str)
            # print(dictionary['boolean_value'])
            return dictionary[key_str]
    elif key_str=="multikey":
        match = re.search(r'({[^{}]*})', text)
        json_str = match.group(1) if match else None
        if json_str:

            dictionary = json.loads(json_str)
            print(dictionary)
            for i in dictionary:
                if "false" in dictionary[i]:
                    dictionary[i]=False
                elif "true" in dictionary[i]:
                    dictionary[i]=True


            print(dictionary)
                    # return i
print(extract_dict(text,"multikey"))