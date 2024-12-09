from ex_5.core import create_seq, locate_seq


command = input()
sequence = []

while command != 'Stop':
    current_command = command.split()
    if current_command[0] == 'Create':
        create_count = int(current_command[2])
        sequence = create_seq(create_count)
        print(sequence)

    elif current_command[0] == 'Locate':
        locate_num = int(current_command[1])
        print(locate_seq(locate_num, sequence))

    command = input()