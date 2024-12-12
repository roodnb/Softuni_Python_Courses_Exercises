directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

n = int(input())
matrix = []
player_row = 0
player_col = 0
stars = 2

for row in range(n):
    line = list(input().split(' '))
    if 'P' in line:
        player_row = row
        player_col = line.index('P')
    matrix.append(line)
matrix[player_row][player_col] = '.'

while True:
    command = input()
    new_row = player_row + directions[command][0]
    new_col = player_col + directions[command][1]
    old_player_row = player_row
    old_player_col = player_col

    if new_row < 0 or new_row >= n or new_col < 0 or new_col >= n:
        new_row = 0
        new_col = 0

    player_row = new_row
    player_col = new_col

    if matrix[new_row][new_col] == "*":
        stars += 1
        matrix[new_row][new_col] = '.'

    if stars >= 10:
        matrix[new_row][new_col] = "P"
        print("You won! You have collected 10 stars.")
        break

    if matrix[new_row][new_col] == "#":
        stars -= 1
        player_row = old_player_row
        player_col = old_player_col

    if stars <= 0:
        matrix[player_row][player_col] = "P"
        print("Game over! You are out of any stars.")
        break


print(f"Your final position is [{player_row}, {player_col}]")

for r in matrix:
    print(*r, sep=' ')