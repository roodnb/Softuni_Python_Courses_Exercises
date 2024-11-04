time_the_car_needs = input().split()
time_car_needs_int = []
for time in time_the_car_needs:
    time_car_needs_int.append(int(time))
left_car_time = time_car_needs_int[:len(time_car_needs_int) // 2]
right_car_time = time_car_needs_int[len(time_car_needs_int) // 2 + 1:]
revers_right = right_car_time[:: -1]
left_car_sum = 0
right_car_sum = 0
for left in left_car_time:
    if left == 0:
        left_car_sum *= 0.8
    left_car_sum += left
for right in revers_right:
    if right == 0:
        right_car_sum *= 0.8
    right_car_sum += right
if left_car_sum < right_car_sum:
    print(f'The winner is left with total time: {left_car_sum:.1f}')
else:
    print(f'The winner is right with total time: {right_car_sum:.1f}')


### posible another way to reverse is in the for cycle for right in right_car_time[mid+1:][::-1]: