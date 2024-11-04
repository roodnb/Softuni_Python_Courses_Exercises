def add_first(first_sequence, values):
    for value in values:
        first_sequence.add(int(value))
    return first_sequence


def add_second(second_sequence, values):
    for value in values:
        second_sequence.add(int(value))
    return second_seq


def remove_first(first_sequence, values):
    for value in values:
        first_sequence.discard(int(value))
    return first_sequence


def remove_second(second_sequence, values):
    for value in values:
        second_sequence.discard(int(value))
    return second_sequence


def check_status(first_sequence, second_sequence):
    if first_sequence >= second_sequence or first_sequence <= second_sequence:
        print('True')
    else:
        print('False')


first_seq = set(map(int, input().split()))
second_seq = set(map(int, input().split()))
num_commands = int(input())

for _ in range(num_commands):
    command = input().split()
    if command[0] == "Add":
        set_number = command[1]
        if set_number == 'First':
            add_first(first_seq, command[2:])
        else:
            add_second(second_seq, command[2:])

    elif command[0] == 'Remove':
        set_number = command[1]
        if set_number == 'First':
            remove_first(first_seq, command[2:])
        else:
            remove_second(second_seq, command[2:])

    elif command[0] == "Check":
        check_status(first_seq, second_seq)

print(*sorted(first_seq), sep=', ')
print(*sorted(second_seq), sep=', ')


# another example
#
# first_seq = set(map(int, input().split()))
# second_seq = set(map(int, input().split()))
# num_commands = int(input())
#
# for _ in range(num_commands):
#     command = input().split()
#     cmd = f'{command[0]} {command[1]}'
#     numbers = [number for number in command[2:]]
#
#     if cmd == "Add First":
#         first_seq.update(numbers)
#     elif cmd == "Add Second":
#         second_seq.update(numbers)
#     elif cmd == 'Remove First':
#         first_seq.difference_update(numbers)
#     elif cmd == 'Remove Second':
#         second_seq.difference_update(numbers)
#     elif cmd == "Check Substet":
#         print(first_seq.issubset(second_seq) or second_seq.issubset(first_seq))
#
# print(*sorted(first_seq), sep=', ')
# print(*sorted(second_seq), sep=', ')