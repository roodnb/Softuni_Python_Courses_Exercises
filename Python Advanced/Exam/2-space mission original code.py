directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

n = int(input())

matrix = []
ship_row = 0
ship_col = 0
resources = 100
planet_reached = False

for row_index in range(n):
    row_data = list(input().split())
    if "S" in row_data:
        ship_col = row_data.index("S")
        ship_row = row_index
    matrix.append(row_data)
matrix[ship_row][ship_col] = '.'


while True:
    command = input()
    new_row = ship_row + directions[command][0]
    new_col = ship_col + directions[command][1]

    last_known_row = ship_row
    last_known_col = ship_col

    ship_row = new_row
    ship_col = new_col

    resources -= 5

    if matrix[new_row][new_col] == "R":
        resources += 10
        if resources > 100:
            resources = 100

    if matrix[new_row][new_col] == "M":
        resources -= 5
        matrix[new_row][new_col] = "."

    if resources < 5 and matrix[new_row][new_col] != "P":
        print(f"Mission failed! The spaceship was stranded in space.")
        break

    if new_row < 0 or new_row >= n or new_col < 0 or new_col >= n:
        print(f"Mission failed! The spaceship was lost in space.")
        ship_row = last_known_row
        ship_col = last_known_col
        break

    if matrix[new_row][new_col] == 'P':
        print(f"Mission accomplished! The spaceship reached Planet B with {resources} resources left.")
        planet_reached = True
        break


if not planet_reached:
    matrix[ship_row][ship_col] = "S"

for line in matrix:
    print(" ".join(line))
