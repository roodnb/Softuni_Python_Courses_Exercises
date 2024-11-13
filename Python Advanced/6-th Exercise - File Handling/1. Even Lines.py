with open(".\\ex_1\\text.txt") as file:
    current_string = file.readlines()
    for index in range(len(current_string)):
        if index % 2 == 0:
            current_string[index] = ((current_string[index].replace('-', '@')
                                    .replace(',', '@')
                                    .replace('.', '@')
                                    .replace('!', '@')
                                    .replace('?', '@'))
                                    .replace('\n', ''))
            line = current_string[index].split()
            print(' '.join(line[::-1]))



# another resolution with regex

import re
with open(".\\ex_1\\text.txt") as file:
    current_string = file.readlines()
    for i in range(0, len(current_string), 2):
        line = reversed(re.sub("[-,.!?]", "@", current_string[i]).split())
        print(*line)
