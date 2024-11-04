# input_string = input().split(', ')
# my_dictionary = {}
# for index in input_string:
#     my_dictionary[index] = ord(index)
# print(my_dictionary)


input_string = input().split(', ')
my_dictionary = {key: ord(key) for key in input_string}
print(my_dictionary)