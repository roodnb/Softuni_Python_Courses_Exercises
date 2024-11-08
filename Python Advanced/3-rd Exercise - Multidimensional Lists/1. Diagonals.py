n = int(input())

matrix = []
for row in range(n):
    lines = [int(x) for x in input().split(', ')]
    matrix.append(lines)

prime_sum = 0
prime_diag = []
for prime_row in range(len(matrix)):
    prime_sum += matrix[prime_row][prime_row]
    prime_diag.append(str(matrix[prime_row][prime_row]))

secondary_sum = 0
secondary_diag = []
for row in range(len(matrix)):
    sec_row = row
    sec_line = abs(row - len(matrix) + 1)
    secondary_sum += matrix[sec_row][sec_line]
    secondary_diag.append(str(matrix[sec_row][sec_line]))

"""Another example
prime = []
secondary = []

for i,j in zip(range(0, len(matrix)), range(len(matrix) -1, -1, -1)):
    а = matrix[i][i]
    b = matrix[i][j]
"""


print(f"Primary diagonal: {', '.join(prime_diag)}. Sum: {prime_sum}")
print(f"Secondary diagonal: {', '.join(secondary_diag)}. Sum: {secondary_sum}")