class InvalidColumnError(Exception):
    pass


class FullColumnError(Exception):
    pass


def print_board(brd):
    for row in brd:
        print(row)


def validate_column(col, max_col):
    if not (0 <= col <= max_col):
        raise InvalidColumnError


def place_player_choice(brd, col, player_n):
    r_count = len(brd)
    for row_index in range(r_count - 1, -1, -1):
        cur_el = brd[row_index][col]
        if cur_el == 0:
            brd[row_index][col] = player_n
            return row_index, col
    raise FullColumnError


def is_winner():
    # TODO
    pass


rows_count = 6
cols_count = 7
board = [[0 for c in range(cols_count)] for r in range(rows_count)]
print_board(board)


player_num = 0
while True:
    player_num = 2 if player_num % 2 == 0 else 1
    try:
        column_num = int(input(f"Player {player_num}, please choose a column: ")) -1
        validate_column(column_num, cols_count - 1)
        row, col = place_player_choice(board, column_num, player_num)
        print_board(board)
        if is_winner():
            print(f'The winner is player {player_num}')
            break
    except (InvalidColumnError, FullColumnError):
        print('Please select a a valid column between [1-7] or column with empty position')
        continue
    except ValueError:
        print('This is not a digit!Please select a a valid column between [1-7]')
        continue
    player_num += 1