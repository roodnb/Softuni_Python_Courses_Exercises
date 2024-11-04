text = input()
digits = ''
alpha = ''
for i in text:
    if i.isnumeric():
        digits += i
        text = text.replace(i, '')

for j in text:
    if j.isalpha():
        alpha += j
        text = text.replace(j, '')

print(digits)
print(alpha)
print(text)


# Another solution:

# text = input()
# digits = ''
# alpha = ''
# other = ''
# for i in text:
#     if i.isnumeric():
#         digits += i
#     elif i.isalpha():
#         alpha += i
#     else:
#         other += i
#
# print(digits)
# print(alpha)
# print(other)