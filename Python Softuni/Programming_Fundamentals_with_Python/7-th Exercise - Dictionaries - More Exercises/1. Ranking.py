contest_password = {}
while True:
    command = input()
    if command == 'end of contests':
        break
    new_command = command.split(':')
    contest = new_command[0]
    password = new_command[1]
    if contest not in contest_password.keys():
        contest_password[contest] = password

second_command = input()
contest_user_points = {}
while second_command != 'end of submissions':

    current_command = second_command.split('=>')

    current_contest = current_command[0]
    current_password = current_command[1]
    username = current_command[2]
    points = int(current_command[3])

    if current_contest in contest_password.keys() and current_password == contest_password[current_contest]:
        if current_contest not in contest_user_points.keys():
            contest_user_points[current_contest] = {}
            contest_user_points[current_contest][username] = points
        elif username not in contest_user_points[current_contest].keys():
            contest_user_points[current_contest][username] = points
        else:
            if points > contest_user_points[current_contest][username]:
                contest_user_points[current_contest][username] = points

    second_command = input()

total_points = {}
for course, user_points in contest_user_points.items():
    for current_user, current_point in user_points.items():
        if current_user not in total_points.keys():
            total_points[current_user] = 0
        total_points[current_user] += current_point

sorted_best_user = dict(sorted(total_points.items(), key=lambda x: x[1], reverse=True))

print(f"Best candidate is {list(sorted_best_user.keys())[0]} with total {max(total_points.values())} points.")
print('Ranking:')
sorted_names = list(sorted(total_points.keys()))
for current_student in sorted_names:
    sorted_grades = {}
    for key, value in contest_user_points.items():
        for nested_key, nested_value in value.items():
            if nested_key == current_student:
                sorted_grades[key] = nested_value
    print(f'{current_student}')
    last_dict = dict(sorted(sorted_grades.items(), key=lambda x: x[1], reverse=True))
    for key1, value1 in last_dict.items():
        print(f'#  {key1} -> {value1}')