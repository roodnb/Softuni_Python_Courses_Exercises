if current_command == 'move':
    new_row = your_row + directions[direction][0] * int(command[2])
    new_col = your_col + directions[direction][1] * int(command[2])
    if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix) and matrix[new_row][new_col] == '.':
        your_row = new_row
        your_col = new_col





    if current_command == 'move':
        for step in range(int(command[2])):
            new_row = your_row + directions[direction][0]
            new_col = your_col + directions[direction][1]
            if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix) and matrix[new_row][new_col] == '.':
                your_row = new_row
                your_col = new_col