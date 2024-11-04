rows, columns = map(int, input().split(', '))

matrix = []
current_sum = 0
for row in range(rows):
    matrix.append([])
    elements = list(map(int, input().split(', ')))
    start_index = 0
    for col in range(columns):
        matrix[row].append(elements[start_index])
        start_index += 1
    current_sum += sum(matrix[row])

print(current_sum)
print(matrix)


# another way:
#
# for row in range(rows):
#     lines = [int(x) for x in input().split(", ")]
#     matrix.append(lines)