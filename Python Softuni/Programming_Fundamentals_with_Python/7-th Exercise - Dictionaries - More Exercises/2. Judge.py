command = input()
contest_dictionary = {}
users = {}


while command != 'no more time':

    current_command = command.split(' -> ')

    username = current_command[0]
    contest = current_command[1]
    points = int(current_command[2])

    if contest not in contest_dictionary:
        contest_dictionary[contest] = {}
        contest_dictionary[contest][username] = points
    elif username not in contest_dictionary[contest]:
        contest_dictionary[contest][username] = points
    elif points > contest_dictionary[contest][username]:
        contest_dictionary[contest][username] = points

    if username not in users:
        users[username] = {contest: points}
    elif contest not in users[username]:
        users[username][contest] = points
    elif users[username][contest] < points:
        users[username][contest] = points

    command = input()

for key, value in contest_dictionary.items():
    print(f'{key}: {len(value.keys())} participants')
    sorted_dict = dict(sorted(value.items(), key=lambda x: x[1], reverse=True))
    i = 1
    for key1, value1 in sorted_dict.items():
        print(f'{i}. {key1} <::> {value1}')
        i += 1

print('Individual standings:')

sorted_names = dict(sorted(users.items(), key=lambda x: (-sum(x[1].values()), x[0])))
i = 1
for k, v in sorted_names.items():
    print(f'{i}. {k} -> {sum(v.values())}')
    i += 1