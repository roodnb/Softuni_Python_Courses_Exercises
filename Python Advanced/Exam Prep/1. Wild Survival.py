from math import floor
from collections import deque

bee_group = deque(map(int, input().split()))
bee_eaters_group = list(map(int, input().split()))


while len(bee_group) != 0 and len(bee_eaters_group) != 0:
    current_bee_grp = bee_group[0]
    current_bee_eater_grp = bee_eaters_group[-1]

    if current_bee_eater_grp * 7 < current_bee_grp:
        remaining_bees = current_bee_grp - current_bee_eater_grp * 7
        bee_group.popleft()
        bee_group.append(remaining_bees)
        bee_eaters_group.pop()

    elif current_bee_eater_grp * 7 == current_bee_grp:
        bee_group.popleft()
        bee_eaters_group.pop()

    else:
        bee_eaters_required = floor(current_bee_grp / 7)

        remaining_eaters = current_bee_eater_grp - bee_eaters_required
        bee_group.popleft()
        bee_eaters_group.pop()
        bee_eaters_group.append(remaining_eaters)


print("The final battle is over!")

if len(bee_group) == 0 and len(bee_eaters_group) == 0:
    print("But no one made it out alive!")

elif bee_group:
    print(f"Bee groups left: {', '.join(str(x) for x in bee_group)}")
elif bee_eaters_group:
    print(f"Bee-eater groups left: {', '.join(str(x) for x in bee_eaters_group)}")
