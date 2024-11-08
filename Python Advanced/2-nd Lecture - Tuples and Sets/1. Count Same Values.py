numbers = tuple(map(float, input().split()))

num_occurance = {}
for num in numbers:
    if num not in num_occurance:
        num_occurance[num] = 0
    num_occurance[num] += 1

# another better approach here
# for num in numbers:
#     num_occurance[num] = numbers.count(num)


for k, v in num_occurance.items():
    print(f"{k} - {v} times")