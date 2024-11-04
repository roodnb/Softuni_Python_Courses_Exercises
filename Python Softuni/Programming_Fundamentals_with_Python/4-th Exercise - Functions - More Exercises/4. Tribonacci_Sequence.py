def tribonacci_sequence(n):
    tribo_list = []
    for num in range(1, n+1):
        if num == 1 or num == 2:
            tribo_list.append(1)
        elif num == 3:
            tribo_list.append(2)
        elif num == 4:
            tribo_list.append(4)
        else:
            tribo_list.append(tribo_list[-3] + tribo_list[-2] + tribo_list[-1])
    return tribo_list


number = int(input())
for final_number in tribonacci_sequence(number):
    print(f'{final_number}', end=' ')