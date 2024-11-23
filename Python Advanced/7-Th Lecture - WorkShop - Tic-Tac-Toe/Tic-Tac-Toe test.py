from math import ceil


class InvalidNumError(Exception):
    pass


class InvalidNumValue(Exception):
    pass


class UnavailablePosition(Exception):
    pass


def valid_position(current_position, current_board):
    try:
        current_position = int(current_position)
    except ValueError:
        raise InvalidNumError
    if current_position < 1 or current_position > 9:
        raise InvalidNumValue
    row = ceil(current_position / 3) - 1
    col = current_position % 3 - 1
    if current_board[row][col] != ' ':
        raise UnavailablePosition
    return current_position, row, col


player_one_name = input("Player one name: ")
player_two_name = input("Player two name: ")
board = [['', '', ''], ['', '', ''], ['', '', '']]

while True:
    player_one_sign = input(f"{player_one_name} would you like to play with 'X' or 'O'?").upper()
    if player_one_sign in ('X', 'O'):
        break

player_two_sign = 'X' if player_one_sign == 'O' else "O"
player_one = (player_one_name, player_one_sign)
player_two = (player_two_name, player_two_sign)

num_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for r in num_board:
    print(f"|  {'  |  '.join([str(ele) for ele in r])}  |")
print(f"{player_one[0]} starts first!")


turns = 1
while True:
    current_player = player_one if turns % 2 != 0 else player_two
    position = input(f'{current_player[0]} choose a free position [1-9]: ')

    try:
        position, row_index, col_index = valid_position(position, board)
    except (InvalidNumValue, InvalidNumError, UnavailablePosition):
        print("Position must be a valid number between [1-9] and should be available space.")
        continue
    else:
        board[row_index][col_index] = current_player[1]
        turns += 1


