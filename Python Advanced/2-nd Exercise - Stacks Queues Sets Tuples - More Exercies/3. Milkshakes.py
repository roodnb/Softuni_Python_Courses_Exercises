from collections import deque

chocolates = list(map(int, input().split(', ')))
cups_of_milk = deque(map(int, input().split(', ')))

milkshakes_done = 0

while chocolates and cups_of_milk and milkshakes_done < 5:
    if chocolates[-1] <= 0 and cups_of_milk[0] <= 0:
        chocolates.pop()
        cups_of_milk.popleft()
        continue
    if chocolates[-1] <= 0:
        chocolates.pop(-1)
        continue
    if cups_of_milk[0] <= 0:
        cups_of_milk.popleft()
        continue
    if chocolates[-1] == cups_of_milk[0]:
        chocolates.pop(-1)
        cups_of_milk.popleft()
        milkshakes_done += 1
    else:
        cups_of_milk.rotate(-1)
        chocolates[-1] -= 5


if milkshakes_done == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(([str(n) for n in chocolates]))}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join(([str(n) for n in cups_of_milk]))}")
else:
    print("Milk: empty")