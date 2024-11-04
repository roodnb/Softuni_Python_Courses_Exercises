rows = int(input())


while True:
    command = input().split()
    if command[0] == "END":
        break

    current_command = command[0]
    row = int(command[1])
    col = int(command[2])
    value = int(command[3])

    if current_command == 'Add' and row in range(0, rows) and col in range(0,rows):
        matrix[row][col] += value
    elif current_command == 'Subtract' and row in range(0, rows) and col in range(0, rows):
        matrix[row][col] -= value
    else:
        print("Invalid coordinates")

for i in matrix:
    print(' '.join(str(ele) for ele in i))