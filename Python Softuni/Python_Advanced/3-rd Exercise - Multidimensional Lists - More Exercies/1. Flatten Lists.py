matrix = [[ele for ele in i.split()] for i in input().split('|')]
sorted_matrix = matrix[::-1]
flat_matrix = [num for sublist in sorted_matrix for num in sublist]
print(' '.join(flat_matrix))