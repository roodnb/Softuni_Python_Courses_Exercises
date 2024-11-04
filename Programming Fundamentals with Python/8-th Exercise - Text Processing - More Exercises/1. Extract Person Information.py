number_of_lines = int(input())

for line in range(number_of_lines):
    data = input().split()
    name = ''
    age = ''
    for item in data:
        if '@' in item:
            if name != '':
                name = ''
            for next_chars in range(item.index('@'), len(item) - 1):
                if item[next_chars] == '@':
                    continue
                if item[next_chars] == '|':
                    break
                name += item[next_chars]

        if '#' in item:
            if age != '':
                age = ''
            for next_chars in range(item.index('#'), len(item) - 1):
                if item[next_chars] == '#':
                    continue
                if item[next_chars] == '*':
                    break
                age += item[next_chars]
        if name != '' and age != '':
            print(f"{name} is {age} years old.")
            name = ''
            age = ''