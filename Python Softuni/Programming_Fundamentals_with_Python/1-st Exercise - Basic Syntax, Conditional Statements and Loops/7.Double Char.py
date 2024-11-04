command = input()

while command != 'End':
    if command != "SoftUni":
        for character in command:
            print(character*2, end='')
        print() # this print is to print every for loop in new line
    command = input()


'''
another example :

    if command != "SoftUni":
        new_string = ''
        for character in command:
            new_string += character * 2 #+= does a concatenation
        print(new_string)
        

'''