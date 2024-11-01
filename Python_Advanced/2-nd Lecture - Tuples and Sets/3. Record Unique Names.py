number_of_names = int(input())
names = []

for _ in range(number_of_names):
    names.append(input())

unique_names = set(names)
print('\n'.join(unique_names))




# another solution
#
# number_of_names = int(input())
# unique_names = set()
# for i in range(number_of_names):
#     unique_names.add(input())
# print('\n'.join(unique_names))