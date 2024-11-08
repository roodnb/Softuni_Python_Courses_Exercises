rows, columns = map(int, input().split())
matrix = []
surrounding_letter = 97
middle_letter = 97
for r in range(rows):
    matrix.append([])
    for c in range(columns):
        cur_let = chr(surrounding_letter)
        mid_let = chr(middle_letter)
        matrix[r].append(cur_let+mid_let+cur_let)
        middle_letter += 1
    surrounding_letter += 1
    middle_letter = surrounding_letter

for submatrix in matrix:
    print(' '.join(submatrix))