directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)}

matrix = []
your_row = 0
your_col = 0
targets = 0

for r in range(5):
    matrix.append(input().split())
    for c in range(5):
        if matrix[r][c] == 'A':
            your_row = r
            your_col = c
        elif matrix[r][c] == 'x':
            targets += 1

hit_targets = []
for i in range(int(input())):
    command = input().split()
    current_command = command[0]
    direction = command[1]

    if current_command == 'move':
        new_row = your_row + directions[direction][0] * int(command[2])
        new_col = your_col + directions[direction][1] * int(command[2])
        if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix) and matrix[new_row][new_col] == '.':
            your_row = new_row
            your_col = new_col


    # Да се прочете мн добре условието на задачаката. Казва се че трябва да идем на полето което е на някви стъпки от нас.
    # в долния пример аз проверявам дали всяко поле до крайната цел е точка. а то не се иска това.
    # if current_command == 'move':
    #     for step in range(int(command[2])):
    #         new_row = your_row + directions[direction][0]
    #         new_col = your_col + directions[direction][1]
    #         if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix) and matrix[new_row][new_col] == '.':
    #             your_row = new_row
    #             your_col = new_col

    elif current_command == "shoot":
        next_shoot_row = your_row + directions[direction][0]
        next_shoot_col = your_col + directions[direction][1]
        while 0 <= next_shoot_row < len(matrix) and 0 <= next_shoot_col < len(matrix):
            if matrix[next_shoot_row][next_shoot_col] == "x":
                matrix[next_shoot_row][next_shoot_col] = "."
                hit_targets.append([next_shoot_row, next_shoot_col])
                targets -= 1
                break
            next_shoot_row += directions[direction][0]
            next_shoot_col += directions[direction][1]

        if targets == 0:
            print(f"Training completed! All {len(hit_targets)} targets hit.")
            break

if targets > 0:
    print(f"Training not completed! {targets} targets left.")

for target in hit_targets:
    print(target)