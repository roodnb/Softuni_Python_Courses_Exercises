from string import punctuation


with open(".\\ex_2\\text.txt") as file, open(".\\ex_2\\output.txt", 'w') as output:
    result = []
    for row, line in enumerate(file.readlines()):
        letters_count = 0
        punctuation_count = 0
        for char in line:
            if char.isalpha():
                letters_count += 1
            elif char in punctuation:
                punctuation_count += 1
        result.append(f'Line {row + 1}: {line[0: -1]} ({letters_count})({punctuation_count})')

    output.write('\n'.join(result))