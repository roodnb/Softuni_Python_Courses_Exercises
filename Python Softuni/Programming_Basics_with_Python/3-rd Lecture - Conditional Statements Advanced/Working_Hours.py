hour = int(input())
day = input()

if 10 <= hour <= 18 and day == ('Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday' or 'Saturday'):
        print('open')
elif day == 'Sunday':
         print('closed')
else:
    print('closed')


'''
moeto reshenie e greshno zashtoto ne moje monday or tusday i taka natatyk
'''

''' 
raboteshto reshenie


hour = int(input())
weekday = input()

if weekday == 'Sunday' or hour < 10 or hour > 18:
    print('closed')
else:
    print('open')
    
'''


'''
drugo reshenie

if day != Sunday
    if 10 <= hour <= 18
     print open
    else
     print closed
else:
    print closed
'''