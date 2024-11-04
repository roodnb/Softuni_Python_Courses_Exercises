numbers = input().split(',')
new_num_list = []

for index in numbers:
    new_num_list.append(int(index))
for i, element in enumerate(new_num_list):
    if element == 0:
        new_num_list[i] = 'None'
        x = new_num_list.count('None')
# for ele in range(0, x):
#     new_num_list.insert(len(new_num_list), 0)
while 'None' in new_num_list:
    new_num_list.remove('None')
    new_num_list.append(0)
print(new_num_list)

