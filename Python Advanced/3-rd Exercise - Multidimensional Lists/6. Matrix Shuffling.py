rows, columns = map(int, input().split())
matrix = [[n for n in input().split()] for i in range(rows)]

while True:
    command = input().split()
    isnotvalid = False
    if command[0] == 'END':
        break
    elif len(command) == 5 and command[0] == 'swap':
        for i in command[1:]:
            if i.isdigit() and 0 <= int(i) <= len(matrix):
                continue
            else:
                print("Invalid input!")
                isnotvalid = True
                break
        if isnotvalid:
            continue
        else:
            row1 = int(command[1])
            col1 = int(command[2])
            row2 = int(command[3])
            col2 = int(command[4])
            first_element = matrix[row1][col1]
            second_element = matrix[row2][col2]

            matrix[row1][col1] = second_element
            matrix[row2][col2] = first_element
            for submatrix in matrix:
                print(' '.join(submatrix))

    else:
        print("Invalid input!")