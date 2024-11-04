sequence = int(input())
uniques = set()
for _ in range(sequence):
    uniques.add(input())
print(*uniques, sep='\n')