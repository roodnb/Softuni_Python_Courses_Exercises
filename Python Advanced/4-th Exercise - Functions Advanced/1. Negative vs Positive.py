def sum_nums(nums):
    p_sum = 0
    n_sum = 0
    for n in numbers:
        if n > 0:
            p_sum += n
        else:
            n_sum += n

    return p_sum, n_sum


numbers = list(map(int, input().split()))

positive, negative = sum_nums(numbers)

print(negative)
print(positive)
if abs(negative) > positive:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")


