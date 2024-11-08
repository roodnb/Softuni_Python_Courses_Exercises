from collections import deque

materials = list(map(int, input().split()))
magic = deque(map(int, input().split()))

gifts = {'Doll': 0, 'Wooden train': 0, 'Teddy bear': 0, 'Bicycle': 0}
items = {150: 'Doll', 250: 'Wooden train', 300: 'Teddy bear', 400: 'Bicycle'}

while materials and magic:
    result = materials[-1] * magic[0]
    if result in items:
        current_present = items[result]
        gifts[current_present] += 1
        materials.pop()
        magic.popleft()
    elif result not in items and result > 0:
        magic.popleft()
        materials[-1] += 15
    elif result == 0:
        if magic[0] == 0:
            magic.popleft()
        if materials[-1] == 0:
            materials.pop()
    else:
        materials.append(materials.pop() + magic.popleft())

if (gifts['Doll'] > 0 and gifts['Wooden train'] > 0) or (gifts['Teddy bear'] > 0 and gifts['Bicycle'] > 0):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join(str(i) for i in reversed(materials))}")
if magic:
    print(f"Magic left: {', '.join(str(j) for j in magic)}")
for k,v in sorted(gifts.items()):
    if v > 0:
        print(f'{k}: {v}',)
