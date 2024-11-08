rows = int(input())
matrix = []
for i in range(rows):
    lines = [int(x) for x in input().split()]
    matrix.append(lines)

total_sum = 0

for index in range(len(matrix)):
    total_sum += matrix[index][index]


# starting_index = 0
# for row in range(len(matrix)):
#     for col in range(len(matrix[row])):
#         total_sum += matrix[row][starting_index]
#         break
#     starting_index += 1

print(total_sum)
