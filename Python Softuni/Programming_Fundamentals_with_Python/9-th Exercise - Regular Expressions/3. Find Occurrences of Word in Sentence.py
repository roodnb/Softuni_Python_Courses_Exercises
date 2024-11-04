import re

text = input()
word_to_search = input()
pattern = fr'(?i)\b{word_to_search}\b'
matches = re.findall(pattern, text)
print(len(matches))




# the below also works , but it gives 80% in judge
# import re
#
# text = input()
# word_to_find = input()
# pattern = r'\b(\w+)\b'
# matches = re.finditer(pattern, text)
# count = 0
# for match in matches:
#     if match.group(1).lower() == word_to_find:
#         count += 1
# print(count)