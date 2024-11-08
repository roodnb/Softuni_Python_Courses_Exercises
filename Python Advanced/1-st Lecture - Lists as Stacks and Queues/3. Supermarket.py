from collections import deque

names_queue = deque()

while True:
    command = input()

    if command == 'Paid':
        for i in range(len(names_queue)):
            print(names_queue.popleft())
    elif command == 'End':
        print(f'{len(names_queue)} people remaining.')
        break
    else:
        names_queue.append(command)
