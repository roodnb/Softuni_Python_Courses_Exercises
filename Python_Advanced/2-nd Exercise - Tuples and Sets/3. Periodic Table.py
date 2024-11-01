count = int(input())

uniques = set()

for _ in range(count):
    elements = input().split()
    uniques.add(ele for ele in elements)

print(*uniques, sep='\n')


# drugo reshenie e :

# for _ in range(count):
#     uniques.update(input().split())


