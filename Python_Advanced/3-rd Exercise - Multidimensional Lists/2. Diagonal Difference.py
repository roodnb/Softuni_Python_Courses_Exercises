matrix = [[int(num) for num in input().split()] for i in range(int(input()))]
prime = []
secondary = []
for i, j in zip(range(0, len(matrix)), range(len(matrix) -1, -1, -1)):
    prime.append(matrix[i][i])
    secondary.append(matrix[i][j])
print(abs(sum(prime) - sum(secondary)))





# The below to be ignored.
# prime_str = []
# secondary_str = []
# for x, y in zip(prime, secondary):
#     if x < 0:
#         prime_str.append(f'({str(x)})')
#     else:
#         prime_str.append(str(x))
#     if y < 0:
#         secondary_str.append(f'({str(y)})')
#     else:
#         secondary_str.append(str(y))
#
# print(f"Primary Diagonal: sum = {' + '.join(prime_str)} = {sum(prime)}")
# print(f"Secondary Diagonal: sum = {' + '.join(secondary_str)} = {sum(secondary)}")
#
# difference = abs(sum(prime) - sum(secondary))
