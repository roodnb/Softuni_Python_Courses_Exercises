each_word = input().split(' | ')
encode_table = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    " ": "SPACE",
}


def decode(letter, table):
    currnet_word = ''
    for key, value in table.items():
        if letter == value:
            currnet_word += key
    return currnet_word


end_result = []
decoded = ''
for word in each_word:
    each_letter = word.split(' ')
    final_word = ''
    for something in each_letter:
        final_word += decode(something, encode_table)
    end_result.append(final_word)

print(' '.join(end_result))


