# tail = input()
# body = input()
# head = input()
# meerkat = [tail, body, head]
# meerkat[0], meerkat[2] = meerkat[2], meerkat[0]
# print(meerkat)



'''
another example
'''

meerkat = []
for body_parts in range(3):
    body_part = input()
    meerkat.append(body_part)

meerkat[0], meerkat[2] = meerkat[2], meerkat[0]
print(meerkat)