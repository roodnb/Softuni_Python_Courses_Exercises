rows, columns = map(int, input().split())
matrix = []
for row in range(rows):
    matrix.append([int(x) for x in input().split()])

max_sum = 0
sub_matrix = None

for row_index in range(rows - 2):
    for col_index in range(columns - 2):
        element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        after_element = matrix[row_index][col_index + 2]
        sum_ele = element + next_element + after_element

        below_element = matrix[row_index + 1][col_index]
        bottom_element = matrix[row_index + 2][col_index]
        sum_below = bottom_element + below_element

        diag_ele = matrix[row_index + 1][col_index + 1]
        diag_after_ele = matrix[row_index + 2][col_index + 2]
        next_diag = matrix[row_index + 1][col_index + 2]
        below_diag = matrix[row_index + 2][col_index + 1]
        sum_diag = diag_after_ele + diag_ele + next_diag + below_diag

        sum_elements = sum_ele + sum_diag + sum_below

        if sum_elements >= max_sum:
            max_sum = sum_elements
            sub_matrix = [[element, next_element, after_element], [below_element, diag_ele, next_diag], [bottom_element, below_diag, diag_after_ele]]

print(f"Sum = {max_sum}")
print(*sub_matrix[0])
print(*sub_matrix[1])
print(*sub_matrix[2])