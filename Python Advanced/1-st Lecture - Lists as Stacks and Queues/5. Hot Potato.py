from collections import deque

kids = deque(input().split(' '))
turns = int(input())
count = 1
while len(kids) > 1:

    if count < turns:
        count += 1
        kid = kids.popleft()
        kids.append(kid)
    else:
        print(f'Removed {kids.popleft()}')
        count = 1

print(f"Last is {''.join(kids)}")