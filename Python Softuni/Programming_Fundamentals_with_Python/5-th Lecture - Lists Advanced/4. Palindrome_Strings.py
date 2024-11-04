def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string


command = input().split(' ')
searched_palindrome = input()
palindrome_list = []
for index in command:
    if is_palindrome(index):
        palindrome_list.append(index)
print(palindrome_list)
print(f'Found palindrome {palindrome_list.count(searched_palindrome)} times')

'''another example


command = input().split(' ')
searched_palindrome = input()

palindrome_list = [word for word in command if word == word[::-1]
palindrome_counter = palindrome_list.count(searched_palindrome
'''
