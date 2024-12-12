directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

n = int(input())

matrix = []
bee_position = None
bee_energy = 15
collected_nectar = 0
energy_restore = False

for row_index in range(n):
    row_data = list(input())
    if "B" in row_data:
        col_index = row_data.index("B")
        bee_position = (row_index, col_index)
    matrix.append(row_data)


while True:
    command = input()

    bee_position_row, bee_position_col = bee_position
    new_row = bee_position_row + directions[command][0]
    new_col = bee_position_col + directions[command][1]

    # dolnoto moje da se smetne i s modulno delenie naprimer
    # new_row = my_position_row + directions[command][0]
    # new_col = my_position_col + directions[command][1]
    # realno pri modulnoto delenie , e vajen ostatyka i kakwo stava , ako delim 2 % 5 nqma ostatyk
    # obache ako delim 5 % 5 imame ostatyk 0 , ako delim 6 % 5 imame ostatyk 1.

    # if new_row < 0:
    #     new_row = sq_mtrx_side - 1
    # elif new_row > sq_mtrx_side - 1:
    #     new_row = 0
    # if new_col < 0:
    #     new_col = sq_mtrx_side - 1
    # elif new_col > sq_mtrx_side - 1:
    #     new_col = 0

    new_row = new_row % n
    new_col = new_col % n

    element = matrix[new_row][new_col]
    matrix[bee_position_row][bee_position_col] = '-'
    matrix[new_row][new_col] = 'B'
    bee_position = (new_row, new_col)

    bee_energy -= 1

    if element.isdigit():
        collected_nectar += int(element)

    elif element == "H":
        if collected_nectar >= 30:
            print(f"Great job, Beesy! The hive is full. Energy left: {bee_energy}")
        else:
            print("Beesy did not manage to collect enough nectar.")
        break

    if bee_energy <= 0 and collected_nectar < 30:
        print("This is the end! Beesy ran out of energy.")
        break

    if bee_energy <= 0 and collected_nectar >= 30 and not energy_restore:
        diff = collected_nectar - 30
        bee_energy += diff
        collected_nectar = 30
        energy_restore = True

    if bee_energy <= 0:
        print("This is the end! Beesy ran out of energy.")
        break


for r in matrix:
    print(*r, sep='')