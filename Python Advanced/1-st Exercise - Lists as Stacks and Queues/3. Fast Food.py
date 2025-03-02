from collections import deque

food_quantity = int(input())
orders = deque(int(x) for x in input().split())
print(max(orders))

while orders and orders[0] <= food_quantity:
    food_quantity -= orders.popleft()

if orders:
    print(f"Orders left: {' '.join(str(order) for order in orders)}")
    # another print way is:
    # print("Orders left:", *orders)
else:
    print("Orders complete")