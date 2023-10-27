import re

import pyperclip


def extract_numbers_from_multiline(text):
    lines = text.strip().split("\n")
    numbers = []

    for line in lines:
        try:
            number=int((re.findall(r"(\d+) _+", line))[0])
            numbers.append(number)
        except:
            pass
    return numbers


# Test
text = pyperclip.paste()
result = extract_numbers_from_multiline(text)
print(sum(result)*0.04)  # ['23', '56', '89']
