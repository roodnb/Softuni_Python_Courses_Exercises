'''
stop_cycle = False

for h in range(24):
    for m in range(60):
        print(f"{h}:{m}")
        if h == 5 and m == 0:
            stop_cycle = True
            break
    if stop_cycle:
        break

'''






rows = int(input())
for i in range(rows):
    for j in range (rows - i - 1):
        print('*', end='')

    for j in range(i + 1):
        print(j + 1, end='')