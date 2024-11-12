try:
    file = open(".\\ex_1\\text.txt")
    print(file.read())
    print('File found')
    file.close()
except FileNotFoundError:
    print('File not found')

