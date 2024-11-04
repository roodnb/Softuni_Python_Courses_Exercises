value = int(input())

if value < 100:
    print('Less than 100')
elif value >= 100 and value <= 200:  # 100 <= value <= 200
    print('Between 100 and 200')
else:
    print('Greater than 200')
