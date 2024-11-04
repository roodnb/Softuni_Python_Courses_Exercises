set_a, set_b = map(int, input().split())
a_set = set()
b_set = set()


for _ in range(set_a):
    a_set.add(input())

for _ in range(set_b):
    b_set.add(input())

print(*(a_set & b_set), sep='\n')

# Towa moje i da stane s comprehension

# a_set = {input() for _ in range(set_a)}