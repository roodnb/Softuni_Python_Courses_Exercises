# 80/100 but it works
# number_list = list(map(int, input().split(', ')))
# found_indices = []
# for num in number_list:
#     if num % 2 == 0:
#         found_indices.append(number_list.index(num))
# print(found_indices)
#
# 80/100 but it works
# number_list = list(map(int, input().split(', ')))
# found_indices = [number_list.index(num) for num in number_list if num % 2 == 0]
# print(found_indices)



# tva reshenie spored men e dosta bezumno , no qvno iskat da se izprobva vsichko.
number_list = list(map(int, input().split(', ')))
found_indices_or_no = map(lambda num: num if number_list[num] % 2 == 0 else 'no', range(len(number_list)))
#tuka : da mapnem tova koeot e v range9a duljivanata na number list s rezultata ot labdatata, demek ili nomera se deli na 2 ili e no.


even_indices = list(filter(lambda index: index != 'no', found_indices_or_no))
print(even_indices)