with open(".\\ex_3\\my_first_file.txt", 'w') as file:
    file.write('I just created my first file!')


# the above created file will be used to be later deleted in ex_4
with open(".\\ex_3\\my_first_file1.txt", 'w') as file:
    file.write('I just created my second file!')

with open(".\\ex_3\\my_first_file.txt") as file:
    print(file.read())
