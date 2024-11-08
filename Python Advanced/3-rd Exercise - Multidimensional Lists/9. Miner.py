from collections import deque

n = int(input())
commands = deque(input().split())
field = [[ele for ele in input().split() if ele in ["*", "e", "c", "s"]] for x in range(n)]

current_row = None
current_col = None

coal_count = 0
for row in range(len(field)):
    for col in range(len(field)):
        if field[row][col] == 's':
            current_row = row
            current_col = col
        elif field[row][col] == 'c':
            coal_count += 1

while len(commands) > 0 and coal_count > 0:
    current_command = commands.popleft()

    if current_command == 'left':
        if current_col - 1 >= 0:
            current_col -= 1

    elif current_command == 'right':
        if current_col + 1 < len(field):
            current_col += 1

    elif current_command == 'up':
        if current_row - 1 >= 0:
            current_row -= 1

    elif current_command == 'down':
        if current_row + 1 < len(field):
            current_row += 1

    if field[current_row][current_col] == 'c':
        coal_count -= 1
        field[current_row][current_col] = '*'

    elif field[current_row][current_col] == 'e':
        print(f"Game over! ({current_row}, {current_col})")
        exit()

if not coal_count:
    print(f"You collected all coal! ({current_row}, {current_col})")
else:
    print(f"{coal_count} pieces of coal left. ({current_row}, {current_col})")