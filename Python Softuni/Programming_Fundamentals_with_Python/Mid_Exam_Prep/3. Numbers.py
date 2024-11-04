sequence = list(map(int, input().split()))
sequence_sorted = sorted(sequence)
average_number = sum(sequence_sorted) / len(sequence_sorted)
highest_num = [num for num in sequence_sorted if num > average_number]
highest_num_sorted = sorted(highest_num, reverse=True)

count = 0
for index in sequence_sorted:
    if index == average_number:
        count += 1

if count == len(sequence_sorted):
    print('No')
else:
    print(f"{' '.join(map(str, highest_num_sorted)[:5])}")



'''another a better code :
sequence = list(map(int, input().split()))
average_number = sum(sequence_sorted) / len(sequence_sorted)
highest_num = [num for num in sequence_sorted if num > average_number]

if highest_num:
    highers_five_num = sorted(highest_num, reverse=True)[:5]
    print()
else:
    print('No)
'''