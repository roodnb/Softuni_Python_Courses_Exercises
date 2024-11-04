input_number = int(input())

current = 1
stop = False


for row in range(1,input_number + 1):
    for col in range(1, row + 1):
        print(current, end=' ')
        if current == input_number:
            stop = True
            break
        current += 1

    if stop:
        break

    print()
