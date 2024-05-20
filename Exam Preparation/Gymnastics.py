country = input()
device = input()


if country == 'Russia':
    if device == 'ribbon':
        complexity_result = 9.100
        performance_result = 9.400
    elif device == 'hoop':
        complexity_result = 9.300
        performance_result = 9.800
    elif device == 'rope':
        complexity_result = 9.600
        performance_result = 9.00

if country == 'Bulgaria':
    if device == 'ribbon':
        complexity_result = 9.600
        performance_result = 9.400
    elif device == 'hoop':
        complexity_result = 9.550
        performance_result = 9.750
    elif device == 'rope':
        complexity_result = 9.500
        performance_result = 9.400

if country == 'Italy':
    if device == 'ribbon':
        complexity_result = 9.200
        performance_result = 9.500
    elif device == 'hoop':
        complexity_result = 9.450
        performance_result = 9.350
    elif device == 'rope':
        complexity_result = 9.700
        performance_result = 9.150

total_result = complexity_result + performance_result
how_much_to_reach_the_goal = ( 20 - total_result)
actual_percent = (how_much_to_reach_the_goal / 20 ) * 100

print(f'The team of {country} get {total_result:.3f} on {device}.')
print(f'{actual_percent:.2f}%')