first_seq = set(map(int, input().split()))
second_seq = set(map(int, input().split()))
num_commands = int(input())

for _ in range(num_commands):
    command = input().split()
    cmd = f'{command[0]} {command[1]}'
    numbers = [number for number in command[2:]]

    if cmd == "Add First":
        first_seq.update(numbers)
    elif cmd == "Add Second":
        second_seq.update(numbers)
    elif cmd == 'Remove First':
        first_seq.difference_update(numbers)
    elif cmd == 'Remove Second':
        second_seq.difference_update(numbers)
    elif cmd == "Check Substet":
        print(first_seq.issubset(second_seq) or second_seq.issubset(first_seq))

print(*sorted(first_seq), sep=', ')
print(*sorted(second_seq), sep=', ')

if milkshakes_done == 5:
    break
if chocolates[-1] > 0 and cups_of_milk[0] > 0:
    if chocolates[-1] == cups_of_milk[0]:
        chocolates.pop(-1)
        cups_of_milk.popleft()
        milkshakes_done += 1
    elif chocolates[-1] < cups_of_milk[0]:
        cups_of_milk.rotate(-1)
        chocolates[-1] -= 5
else:
    if chocolates[-1] <= 0:
        chocolates.pop(-1)
    if cups_of_milk[0] <= 0:
        cups_of_milk.popleft()