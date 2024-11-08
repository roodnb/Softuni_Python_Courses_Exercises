num_of_guests = int(input())
reservations = set()

for _ in range(num_of_guests):
    reservations.add(input())

while True:
    people_that_came = input()
    if people_that_came == "END":
        break
    else:
        reservations.remove(people_that_came)


print(len(reservations))
for guest in sorted(reservations):
    print(guest)