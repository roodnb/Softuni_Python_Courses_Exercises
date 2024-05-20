input_number = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0


for index in range(0, input_number):
    num = int(input())
    if 0 <= num < 200:
        p1 += 1
    elif 200 <= num < 400:
        p2 += 1
    elif 400 <= num < 600:
        p3 += 1
    elif 600 <= num < 800:
        p4 += 1
    else:
        p5 += 1

print(f'{p1/input_number*100:.2f}%')
print(f'{p2/input_number*100:.2f}%')
print(f'{p3/input_number*100:.2f}%')
print(f'{p4/input_number*100:.2f}%')
print(f'{p5/input_number*100:.2f}%')