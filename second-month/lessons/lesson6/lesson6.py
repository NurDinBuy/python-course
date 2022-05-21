import re

text = 'AV Analytics Vidhya AV'

result = re.match(r'AV', text)
print(result)

result = re.match(r'Analytics', text)
print(result)

result = re.search(r'Analytics', text)
print(result)

result = re.search(r'AV', text)
print(result)

result = re.findall(r'A[Vn]', text)
print(result)

result = re.split(r' ', text)
print(result)

result = re.split(r' ', text, 2)
print(result)

result = re.sub(r'AV', r'HI', text)
print(result)

with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
    beeline_numbers_list = re.findall(r'\+996 77[0-9] [0-9 ]{8}', content)
    print(beeline_numbers_list)
    mega_numbers_list = re.findall(r'\+996 55[0-9] [0-9 ]{8}', content)
    print(mega_numbers_list)
    p = re.compile(r'\+996 (50|70)[0-9] [0-9 ]{8}')
    o_numbers_list = re.findall(r'\+996 [57]0[0-9] [0-9 ]{8}', content)
    print(o_numbers_list)
