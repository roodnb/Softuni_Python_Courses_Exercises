def decipher_this(string):
    deciphered_password = []
    for word in string:
        deciphered_word = []
        new_word = list(word)
        first_letter_lst = []
        for index in new_word:
            try:
                int(index)
                first_letter_lst.append(index)
            except ValueError:
                deciphered_word.append(index)
        first_letter_actual = chr(int(''.join(first_letter_lst)))
        deciphered_word.insert(0, first_letter_actual)
        deciphered_word[1], deciphered_word[-1] = deciphered_word[-1], deciphered_word[1]

        deciphered_password.append(''.join(deciphered_word))

    return ' '.join(deciphered_password)

password = input().split()
print(decipher_this(password))


