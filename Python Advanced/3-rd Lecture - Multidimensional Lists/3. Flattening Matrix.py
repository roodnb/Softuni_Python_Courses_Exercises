rows = int(input())
matrix = []
for row in range(rows):
    matrix.append(list(map(int, input().split(', '))))

flattened_matrix = [element for row in matrix for element in row]

print(flattened_matrix)