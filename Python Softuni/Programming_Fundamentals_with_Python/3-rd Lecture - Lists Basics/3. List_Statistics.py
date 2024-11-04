number = int(input())
positive_list = []
negative_list = []
for num in range(number):
    current_num = int(input())
    if current_num >= 0:
        positive_list.append(current_num)
    else:
        negative_list.append(current_num)

# count_positive = len(positive_list)
# sum_negative = sum(negative_list)
print(positive_list)
print(negative_list)
print(f'Count of positives: {len(positive_list)}')
print(f'Sum of negatives: {sum(negative_list)}')


# print(f'Count of positives: {count_positive}')
# print(f'Sum of negatives: {sum_negative}')
