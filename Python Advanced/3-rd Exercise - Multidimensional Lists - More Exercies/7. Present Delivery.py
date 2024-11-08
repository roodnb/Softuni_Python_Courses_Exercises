directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
m = int(input()) #number of presents
n = int(input()) #neighborhood size

matrix = []
santa = []
nice_kids = 0
total_nice = 0
for r in range(n):
    matrix.append(input().split())
    for c in range(n):
        if matrix[r][c] == 'S':
            santa = [r, c]
        elif matrix[r][c] == 'V':
            nice_kids += 1
            total_nice += 1

while True:
    if m == 0:
        break

    command = input()
    if command == 'Christmas morning':
        break

    new_row = santa[0] + directions[command][0]
    new_col = santa[1] + directions[command][1]

    if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix):
        matrix[santa[0]][santa[1]] = "-"
        if matrix[new_row][new_col] == 'V':
            matrix[new_row][new_col] = '-'
            m -= 1
            nice_kids -= 1
        elif matrix[new_row][new_col] == 'X':
            matrix[new_row][new_col] = '-'
        elif matrix[new_row][new_col] == 'C':
            for direct in directions:
                around_santa_row = new_row + directions[direct][0]
                around_santa_col = new_col + directions[direct][1]
                if m == 0:
                    break
                if 0 <= around_santa_row < len(matrix) and 0 <= around_santa_col < len(matrix) and matrix[around_santa_row][around_santa_col] != '-':
                    m -= 1
                    if matrix[around_santa_row][around_santa_col] == 'V':
                        nice_kids -= 1
                matrix[around_santa_row][around_santa_col] = '-'

            matrix[new_row][new_col] = '-'

        matrix[new_row][new_col] = 'S'
        santa = [new_row, new_col]


if m == 0 and nice_kids > 0:
    print("Santa ran out of presents!")

for lst in matrix:
    print(' '.join(lst))

if nice_kids == 0:
    print(f"Good job, Santa! {total_nice} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids} nice kid/s.")