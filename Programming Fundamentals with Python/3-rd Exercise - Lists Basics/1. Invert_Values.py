numbers = input()
original_list = numbers.split(' ')
numbered_original_list = []
opposite_number_list = []

for num in original_list:
    number = int(num)
    numbered_original_list.append(number)

for number in numbered_original_list:
    opposite_number = number * -1
    opposite_number_list.append(opposite_number)

print(opposite_number_list)


'''
my_list = input().split()
opposite_number = []

for number in my_list:
    opposite_number = -int(number)
    opposite_numbers.append(opposite_number)
    
    
another example    
    
print([-int(number) for number in input().split()])

'''