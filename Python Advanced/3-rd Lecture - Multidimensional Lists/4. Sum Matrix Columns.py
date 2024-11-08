rows, columns = map(int, input().split(', '))
matrix = []
sum_list = []
for row in range(rows):
    lines = [int(x) for x in input().split()]
    matrix.append(lines)


for column_index in range(columns):
    col_sum = 0
    for row_index in range(rows):
        col_sum += matrix[row_index][column_index]
    print(col_sum)


# sum_list.extend(0 for i in range(len(matrix[0])))
# for index in matrix:
#     for j in range(len(index)):
#         sum_list[j] += index[j]
#
# for ele in sum_list:
#     print(ele)


# current_index = 0
# current_sum = 0
# some_counter = 0
# while some_counter != len(matrix[0]):
#     for current_row in matrix:
#         current_sum += current_row[current_index]
#     print(current_sum)
#     current_sum = 0
#     current_index += 1
#     some_counter += 1

