frase = input()
new_frase = ''
for char in frase:
    new_char = ord(char) + 3
    new_frase += chr(new_char)
print(new_frase)