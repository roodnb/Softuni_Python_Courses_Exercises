moves = {
    'top_left': (-2, -1),
    'top_right': (-2, 1),
    'mid_top_left': (-1, -2),
    'mid_top_right': (-1, 2),
    'mid_bot_left': (1, -2),
    'mid_bot_right': (1, 2),
    'bottom_left': (2, -1),
    'bottom_right': (2, 1),
}

rows = int(input())
matrix = []
knights = []

for r in range(rows):
    matrix.append([x for x in input()])
    for c in range(rows):
        if matrix[r][c] == 'K':
            knights.append([r, c])

removed_knights = 0
while True:
    max_hits = 0
    max_knight = [0, 0]

    for k_row, k_col in knights:
        hits = 0
        for move in moves.values():
            next_row = k_row + move[0]
            next_col = k_col + move[1]
            if 0 <= next_row < rows and 0 <= next_col < rows:
                if matrix[next_row][next_col] == 'K':
                    hits += 1

        if hits > max_hits:
            max_hits = hits
            max_knight = [k_row, k_col]

    if max_hits == 0:
        break

    knights.remove(max_knight)
    matrix[max_knight[0]][max_knight[1]] = "0"
    removed_knights += 1

print(removed_knights)