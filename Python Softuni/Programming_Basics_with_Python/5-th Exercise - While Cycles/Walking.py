goal = 10000
steps_taken = 0
steps_over = 0
command = input()

while command != 'Going home':
    steps_to_do = int(command)
    steps_taken += steps_to_do
    if steps_taken >= goal:
        steps_over = steps_taken - goal
        print('Goal reached! Good job!')
        print(f'{steps_over} steps over the goal!')
        break

    command = input()

if command == 'Going home':
    steps_to_home = int(input())
    steps_taken += steps_to_home
    if steps_taken >= goal:
        steps_over = steps_taken - goal
        print('Goal reached! Good job!')
        print(f'{steps_over} steps over the goal!')
    else:
        print(f'{goal-steps_taken} more steps to reach goal.')

'''
Drugo reshenie

goal = 10000
steps_taken = 0

while steps_taken < goal    :
    command = input()
    if command == 'Going home':
        steps_to_do = int(input())
        steps_taken += steps_to_do
        break
    steps_to_do = int(command)
    steps_taken += steps_to_do


if steps_taken >= goal:
    print('Goal reached! Good job!')
    print(f'{steps_taken - goal} steps over the goal!')
else:
    print(f'{goal - steps_taken} more steps to reach goal.')

'''