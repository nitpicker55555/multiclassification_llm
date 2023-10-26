import json
import re
#
# text = """Based on the provided information, it is not clear whether there is a privacy violation in the news. Privacy violations typically involve the unauthorized or inappropriate disclosure of personal information. The information provided in the news article does not explicitly mention a privacy violation. Therefore, the answer is:
# asd
# Based on the information provided in the news, there doesn't appear to be any mention or indication of privacy violation. The incident revolves around an accident with a robot and bear repellent at an Amazon warehouse.
#
# Therefore, the appropriate JSON response would be:
#
# ```json
# {
#     "privacy violation": "False"
# }
#
# ```
# asd
# """


def extract_dict(text,key_str):



            text = text.lower()
            key_str=key_str.lower()
            match = re.search(r'({[^{}]*})', text)
            json_str = match.group(1) if match else None
            print(json_str)

            if key_str!="multikey":

                result =re.sub(r'[^a-zA-Z]', '', json_str)
                key_str=re.sub(r'[^a-zA-Z]', '', key_str)

                print(result,key_str)

                if key_str in result:

                    first_letter = result.replace(key_str,"")
                    print(first_letter)
                    if "f" in first_letter:
                        return False
                    elif "t" in first_letter:
                        return True
                    print(first_letter)
                # else:
                #
                #         text = selenium_spider("please set key value of {'%s'} to true or false"%key_str, True, False)
                #         continue



            elif key_str=="multikey":
                    json_str = re.sub(r"'", '"', json_str)
                    print(json_str)
                    dictionary = json.loads(json_str)
                    for i in dictionary:
                        if not isinstance(dictionary[i], bool):
                            if "false" in dictionary[i]:
                                dictionary[i]=False
                            elif "true" in dictionary[i]:
                                dictionary[i]=True
                    for i in dictionary:
                        if dictionary[i]==True:

                            return i  #return the key is true


    # Parse the JSON string to a Python dictionary
                    # return i
text="""zxcz
{'individual': false, 'local population ': true, 'global': false}
"""

# text = """Based on the provided information, it is not clear whether there is a privacy violation in the news. Privacy violations typically involve the unauthorized or inappropriate disclosure of personal information. The information provided in the news article does not explicitly mention a privacy violation. Therefore, the answer is:
# asd
# Based on the information provided in the news, there doesn't appear to be any mention or indication of privacy violation. The incident revolves around an accident with a robot and bear repellent at an Amazon warehouse.
#
# Therefore, the appropriate JSON response would be:
#
# ```json
# {
#     "privacy violation": "False"
# }
#
# ```
# asd
# """

print(extract_dict(text,"multikey"))