money = input()
count_of_beggars = int(input())
money_list_str = money.split(',')
money_list_int = [] # realno poziciite sys dadenite pari.
for i in money_list_str:
    actual_money = int(i)
    money_list_int.append(actual_money)

final_list = []
starting_index = 0
for current_beggar in range(count_of_beggars):
    each_beggar_money_sum = 0
    for index in range(starting_index, len(money_list_int), count_of_beggars):
        each_beggar_money_sum += money_list_int[index]
    final_list.append(each_beggar_money_sum)
    starting_index += 1

print(final_list)
    

