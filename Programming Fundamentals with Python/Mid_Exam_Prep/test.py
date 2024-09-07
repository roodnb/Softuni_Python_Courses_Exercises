sequence = [int(target) for target in input().split()]
command = input().split()
while command[0] != "End":
    action, index, value = command[0], int(command[1]), int(command[2])
    if action == "Shoot":
        if index in range(len(sequence)):
            sequence[index] -= value
            if sequence[index] <= 0:
                sequence.pop(index)
    elif action == "Add":
        if index in range(len(sequence)):
            sequence.index(index, value)
        else:
            print('Invalid placement!')
    elif action == "Strike":
        if index - value not in range(len(sequence)) \
                or index + value not in range(len(sequence)):
            print('Strike missed!')
        else:
            before_strike = sequence[:index - value]
            after_strike = sequence[index + value + 1:]
            sequence = before_strike + after_strike
    command = input().split()

print(*sequence, sep="|")