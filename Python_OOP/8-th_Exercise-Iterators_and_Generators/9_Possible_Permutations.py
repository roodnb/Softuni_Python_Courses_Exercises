from itertools import permutations


def possible_permutations(my_list: list):
    for perm in permutations(my_list):
        yield list(perm)


[print(n) for n in possible_permutations([1, 2, 3])]

print(f"\n{'-----------------------------NEW TEST CODE-----------------------------'}")

[print(n) for n in possible_permutations([1])]
