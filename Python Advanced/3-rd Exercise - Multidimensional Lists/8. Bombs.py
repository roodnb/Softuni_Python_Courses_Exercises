n = int(input())
matrix = [[int(x) for x in input().split()] for row in range(n)]
idk_crd = input().split()



def reduce_cells(x, y, s, mtrx, curr_bomb: int):
    cells = []
    mtrx[x][y] -= curr_bomb

    if x-1 in range(s) and y-1 in range(s):
        cells.append((x-1, y-1))
    if x-1 in range(s) and y in range(s):
        cells.append((x-1, y))
    if x-1 in range(s) and y+1 in range(s):
        cells.append((x-1, y+1))

    if x in range(s) and y-1 in range(s):
        cells.append((x, y-1))
    if x in range(s) and y+1 in range(s):
        cells.append((x, y+1))

    if x+1 in range(s) and y-1 in range(s):
        cells.append((x+1, y-1))
    if x+1 in range(s) and y in range(s):
        cells.append((x+1, y))
    if x+1 in range(s) and y+1 in range(s):
        cells.append((x+1, y+1))

    for position in cells:
        r = position[0]
        c = position[1]
        if mtrx[r][c] > 0:
            mtrx[r][c] -= curr_bomb


for bomb in idk_crd:
    row, col = map(int, bomb.split(','))
    current_bomb = matrix[row][col]
    if current_bomb > 0:
        reduce_cells(row, col, n, matrix, current_bomb)

live_sum = 0
for lst in matrix:
    for ele in lst:
        if ele > 0:
            live_sum += ele

live_count = 0
for lstt in matrix:
    for elem in lstt:
        if elem > 0:
            live_count += 1

print(f"Alive cells: {live_count}")
print(f"Sum: {live_sum}")
for entry in matrix:
    print(' '.join(str(ele) for ele in entry))
