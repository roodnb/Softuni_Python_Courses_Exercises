from collections import deque

bees = deque(map(int, input().split()))
nectar = list(map(int, input().split()))
process = deque(input().split())
total_honey = 0

while bees and nectar:
    if nectar[-1] >= bees[0]:
        proc = process.popleft()
        bee = bees.popleft()
        nec = nectar.pop()
        if proc == "+":
            total_honey += abs(bee + nec)
        elif proc == '-':
            total_honey += abs(bee - nec)
        elif proc == '*':
            total_honey += abs(bee * nec)
        elif proc == '/':
            if nec == 0:
                continue
            else:
                total_honey += abs(bee / nec)
    else:
        nectar.pop()

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(str(i) for i in bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(j)for j in nectar)}")