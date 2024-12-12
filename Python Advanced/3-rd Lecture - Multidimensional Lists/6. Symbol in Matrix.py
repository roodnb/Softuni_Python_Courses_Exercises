n = int(input())
matrix = []
for i in range(n):
    matrix.append(input())



symbol = input()

for i in range(n):
    for j in range(n):
        if matrix[i][j] == symbol:
            print(f"({i}, {j})")
            exit()

print(f'{symbol} does not occur in the matrix')