numbers = int(input())
odd_set = set()
even_set = set()
for num in range(numbers):
    name = input()
    sum_name = sum(ord(i) for i in name) // (num + 1)
    if sum_name % 2 == 0:
        even_set.add(sum_name)
    else:
        odd_set.add(sum_name)

if sum(odd_set) == sum(even_set):
    print(*(even_set | odd_set), sep=', ')
elif sum(odd_set) > sum(even_set):
    print(*(odd_set - even_set), sep=', ')
elif sum(odd_set) < sum(even_set):
    print(*(odd_set ^ even_set), sep=', ')