rows, columns = map(int, input().split())

snake = input()

matrix = [['' for _ in range(columns)] for r in range(rows)]
index = 0

for row in range(rows):
    if row % 2 == 0:
        for col in range(columns):
            matrix[row][col] = snake[index]
            index = (index + 1) % len(snake)
    else:
        for col in range(columns - 1, -1, -1):
            matrix[row][col] = snake[index]
            index = (index + 1) % len(snake)

for submatrix in matrix:
    print(''.join(submatrix))