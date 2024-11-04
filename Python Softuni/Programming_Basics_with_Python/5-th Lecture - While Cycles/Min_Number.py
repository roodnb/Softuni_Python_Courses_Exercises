import sys

min_number = sys.maxsize

while True:
    text = input()
    if text == 'Stop':
        break

    num = int(text)
    if num < min_number:
        min_number = num

print(min_number)