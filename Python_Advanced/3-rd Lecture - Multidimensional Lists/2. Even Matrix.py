num = int(input())
result = [[ele for ele in map(int, input().split(', ')) if ele % 2 == 0] for i in range(num)]
print(result)

# num = int(input())
# matrix = []
# for i in range(num):
#     row_data = [int(ele) for ele in input().split() if int(ele) % 2 == 0]
#     matrix.append(row_data)
# print(matrix)

# rows = int(input())
# matrix = []
# for i in range(rows):
# row = input().split(", ")
# matrix.append(list(map(int, row)))
# evens = [[x for x in row if x % 2 == 0] for row in matrix]
# print(evens)