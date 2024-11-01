from collections import deque
bullet_price = int(input())
barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque(int(x) for x in input().split())
intelligence_value = int(input())


bullets_used = 0
current_barrel_size = barrel_size


while bullets and locks:
    current_barrel_size -= 1
    bullets_used += 1
    if locks[0] >= bullets[-1]:
        locks.popleft()
        bullets.pop()
        print('Bang!')
    else:
        bullets.pop()
        print('Ping!')

    if bullets:
        if current_barrel_size == 0:
            current_barrel_size = barrel_size
            print("Reloading!")


money_earned = intelligence_value - (bullet_price * bullets_used)

if len(bullets) >= 0 and len(locks) == 0:
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")