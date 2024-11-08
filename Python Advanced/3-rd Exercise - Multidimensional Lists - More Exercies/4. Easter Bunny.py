directions = {
    'up': [-1, 0, 0],
    'down': [1, 0, 0],
    'left': [0, -1, 0],
    'right': [0, 1, 0],
}

size = int(input())
matrix = []

bunny_r = 0
bunny_c = 0
for r in range(size):
    matrix.append([ele for ele in input().split()])
    for c in range(size):
        if matrix[r][c] == "B":
            bunny_r = r
            bunny_c = c

for move in directions:
    row = bunny_r
    col = bunny_c
    while True:
        new_r = row + directions[move][0]
        new_c = col + directions[move][1]
        if 0 <= new_r < len(matrix) and 0 <= new_c < len(matrix):
            if matrix[new_r][new_c] == 'X':
                break
            directions[move][2] += int(matrix[new_r][new_c])
            directions[move].append([new_r, new_c])
        else:
            break
        row = new_r
        col = new_c

max_sum = 0
path = ''
for summ in directions:
    if directions[summ][2] >= max_sum:
        max_sum = directions[summ][2]
        path = summ

print(path)
for coordinate in directions[path][3:]:
    print(coordinate)
print(max_sum)