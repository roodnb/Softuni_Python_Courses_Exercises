import sys

max_number = -sys.maxsize

while True:
    text = input()
    if text == 'Stop':
        break

    num = int(text)
    if num > max_number:
        max_number = num

print(max_number)