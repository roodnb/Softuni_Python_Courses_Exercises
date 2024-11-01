lines = int(input())
longest_intersection = set()
for line in range(lines):
    first_line, second_line = input().split('-')
    first_start, first_end = map(int, first_line.split(','))
    second_start, second_end = map(int, second_line.split(','))
    first = {num for num in range(first_start, first_end + 1)}
    # first = set(range(first_start, first_end + 1)) - tuk kazvame , vzemi vsichko v toq range i go turi u set. po byrzo e ot for cycle
    second = {num for num in range(second_start, second_end + 1)}
    intersection = first & second
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f'Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}')