def exchange(_initial_list, _index):
    first_half = initial_list[:_index + 1]
    second_half = initial_list[_index + 1:]
    _initial_list = second_half + first_half
    return _initial_list


def maximum(_initial_list, _even_or_odd):
    if _even_or_odd == 'even':
        max_even = max(num for num in _initial_list if num % 2 == 0)
        return max_even
    else:
        max_odd = max(num for num in _initial_list if num % 2 != 0)
        return max_odd


def minimum(_initial_list, _even_or_odd):
    if _even_or_odd == 'even':
        min_even = min(num for num in _initial_list if num % 2 == 0)
        return min_even
    else:
        min_even = min(num for num in _initial_list if num % 2 != 0)
        return min_even


def first(_initial_list, _count, _even_or_odd):
    if _even_or_odd == 'even':
        even_list = [num for num in _initial_list if num % 2 == 0]
        return even_list[:_count - 1]
    else:
        odd_list = [num for num in _initial_list if num % 2 != 0]
        return odd_list[:_count - 1]
        


def last(_initial_list, _count, _even_or_odd):
    if _even_or_odd == 'even':
        even_list = [num for num in _initial_list if num % 2 == 0]
        return even_list[_count - 1:]
    else:
        odd_list = [num for num in _initial_list if num % 2 != 0]
        return odd_list[_count - 1:]


initial_list = [int(num) for num in input().split()]
command = input().split()
while command[0] != 'end':
    action = command[0]
    if action == 'exchange':
        index = int(command[1])
        initial_list = exchange(initial_list, index)
    elif action == 'max':
        even_or_odd = command[1]
        initial_list = maximum(initial_list, even_or_odd)
    elif action == 'min':
        even_or_odd = command[1]
        initial_list = minimum(initial_list, even_or_odd)
    elif action == 'first':
        count = int(command[2])
        even_or_odd = command[3]
        initial_list = first(initial_list, count, even_or_odd)
    elif action == 'last':
        count = int(command[2])
        even_or_odd = command[2]
        initial_list = last(initial_list, count, even_or_odd)
    command = input().split()

print(initial_list)