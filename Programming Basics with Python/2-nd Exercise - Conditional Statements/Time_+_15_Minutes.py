import math

time_hours = int(input())
time_minutes = int(input())
time_hours_to_mins = time_hours * 60

total_minutes = time_minutes + time_hours_to_mins + 15

hours = total_minutes // 60
minutes = total_minutes % 60



if 1440 <= total_minutes < 1450:
    print(f'0:0{minutes}')
elif minutes < 10:
    print(f'{hours}:0{minutes}')
elif hours >= 24:
    print(f'0:{minutes}')
else:
    print(f'{hours}:{minutes}')

# Another much easier example
'''
hours = int(input())
minutes = int(input())

minutes += 15

if minutes >= 60:
    minutes -= 60
    hours += 1

if hours >= 24:
    hours -= 24

if minutes < 10:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")
'''