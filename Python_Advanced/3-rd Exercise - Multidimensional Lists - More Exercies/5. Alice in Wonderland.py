n = int(input())
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)}

matrix = []

alice_row = 0
alice_col = 0

for r in range(n):
    matrix.append([ele for ele in input().split()])
    for c in range(n):
        if matrix[r][c] == 'A':
            alice_row = r
            alice_col = c

tea_bags = 0

while True:
    command = input()
    new_row = alice_row + directions[command][0]
    new_col = alice_col + directions[command][1]
    matrix[alice_row][alice_col] = "*"
    if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix):
        if matrix[new_row][new_col] == 'R':
            matrix[new_row][new_col] = '*'
            print("Alice didn't make it to the tea party.")
            break
        if matrix[new_row][new_col].isdigit():
            tea_bags += int(matrix[new_row][new_col])
            if tea_bags >= 10:
                matrix[new_row][new_col] = '*'
                print("She did it! She went to the party.")
                break

    else:
        print("Alice didn't make it to the tea party.")
        break

    alice_row = new_row
    alice_col = new_col

for row in matrix:
    print(' '.join(row))