import os


try:
    os.remove(".\\ex_3\\my_first_file1.txt")
except FileNotFoundError:
    print('File already deleted!')


