rows, columns = map(int, input().split())
matrix = []
for row in range(rows):
    matrix.append([x for x in input().split()])

square_matrices = 0
for row_index in range(rows - 1):
    for col_index in range(columns - 1):
        element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        below_element = matrix[row_index + 1][col_index]
        diag_ele = matrix[row_index + 1][col_index + 1]

        if element == next_element == below_element == diag_ele:
            square_matrices += 1

print(square_matrices)