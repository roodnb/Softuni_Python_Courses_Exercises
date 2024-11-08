directions = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
}

def spread_bunnies(lair, rows, cols):
    new_lair = [row[:] for row in lair]
    for r in range(rows):
        for c in range(cols):
            if lair[r][c] == 'B':
                for dr, dc in directions.values():
                    new_r, new_c = r + dr, c + dc
                    if 0 <= new_r < rows and 0 <= new_c < cols:
                        new_lair[new_r][new_c] = 'B'
    return new_lair

rows, cols = map(int, input().split())
lair = [list(input()) for _ in range(rows)]
commands = input()

player_row, player_col = 0, 0
for r in range(rows):
    for c in range(cols):
        if lair[r][c] == 'P':
            player_row, player_col = r, c
            lair[r][c] = '.'
            break

game_over = False
for move in commands:
    new_row = player_row + directions[move][0]
    new_col = player_col + directions[move][1]

    lair = spread_bunnies(lair, rows, cols)

    if not (0 <= new_row < rows and 0 <= new_col < cols):
        for row in lair:
            print("".join(row))
        print(f"won: {player_row} {player_col}")
        game_over = True
        break

    if lair[new_row][new_col] == 'B':
        for row in lair:
            print("".join(row))
        print(f"dead: {new_row} {new_col}")
        game_over = True
        break

    player_row, player_col = new_row, new_col

if not game_over:
    for row in lair:
        print("".join(row))
    print(f"dead: {player_row} {player_col}")




























while win == 0 and dead == 0:

    for command in commands:
        if command == 'L':
            if player_col == 0:
                win += 1
            elif player_col - 1 >= 0:
                player_col -= 1
                if matrix[player_row][player_col] == 'B':
                    dead += 1

        elif command == 'R':
            if player_col == columns:
                win += 1
            elif player_col+ 1 <= columns:
                player_col += 1
                if matrix[player_row][player_col] == 'B':
                    dead += 1

        elif command == 'U':
            if player_row == 0:
                win += 1
            elif player_row - 1 >= 0:
                player_row -= 1
                if matrix[player_row][player_col] == 'B':
                    dead += 1

        elif command == 'D':
            if player_row == rows:
                win += 1
            elif player_row + 1 <= rows:
                player_row += 1
                if matrix[player_row][player_col] == 'B':
                    dead += 1


    current_bunnies = []
    for bunny in bunnies:
        bunny_r = bunny[0]
        bunny_c = bunny[1]
        if bunny_c - 1 >= 0 and matrix[bunny_r][bunny_c - 1] != "B":
            matrix[bunny_r][bunny_c - 1] = "B"
            current_bunnies.append([bunny_r, bunny_c - 1])
        if bunny_c + 1 < columns and matrix[bunny_r][bunny_c + 1] != "B":
            matrix[bunny_r][bunny_c + 1] = 'B'
            current_bunnies.append([bunny_r, bunny_c + 1])
        if bunny_r - 1 >= 0 and matrix[bunny_r - 1][bunny_c] != "B":
            matrix[bunny_r - 1][bunny_c] = 'B'
            current_bunnies.append([bunny_r - 1, bunny_c])
        if bunny_r + 1 < rows and matrix[bunny_r + 1][bunny_c] != "B":
            matrix[bunny_r + 1][bunny_c] = 'B'
            current_bunnies.append([bunny_r + 1, bunny_c])

    bunnies.extend(current_bunnies)

for entry in matrix:
    print(''.join(entry))
if win != 0:
    print(f"won: {player_row} {player_col}")
elif dead != 0:
    print(f"dead: {player_row} {player_col}")