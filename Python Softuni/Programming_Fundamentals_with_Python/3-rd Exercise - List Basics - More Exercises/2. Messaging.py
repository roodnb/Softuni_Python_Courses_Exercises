number_sequence = input().split()
frase = input()
frase_lst = []
for index in number_sequence:
    sum_digits = 0
    for number in index:
        sum_digits += int(number)

    sum_digits %= len(frase)
    # if 0 < sum_digits <= len(frase):
    frase_lst.append(frase[sum_digits])
    frase = frase[:sum_digits] + frase[sum_digits+1:]
    # if sum_digits > len(frase):
    #     frase_lst.append(frase[sum_digits - len(frase)])
    #     frase = frase[:sum_digits - len(frase)] + frase[sum_digits - len(frase)+1:]

print(''.join(frase_lst))
