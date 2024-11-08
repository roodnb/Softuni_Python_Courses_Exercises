rows, columns = map(int, input().split(', '))
matrix = []
for row in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

max_sum = 0
sub_matrix = None

for row_index in range(rows - 1):
    for col_index in range(columns - 1):
        element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        below_element = matrix[row_index + 1][col_index]
        diag_ele = matrix[row_index + 1][col_index + 1]

        sum_elements = element + next_element + below_element + diag_ele
        if sum_elements > max_sum:
            max_sum = sum_elements
            sub_matrix = [[element, next_element], [below_element, diag_ele]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)