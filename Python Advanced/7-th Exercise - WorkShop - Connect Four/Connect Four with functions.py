# Position mapper
position_map = [
    {'D': (1, 0), 'DD': (2, 0), 'DDD': (3, 0)},
    {'L': (0, -1), 'LL': (0, -2), 'LLL': (0, -3)},
    {'R': (0, 1), 'RR': (0, 2), 'RRR': (0, 3)},
    {'LD_U': (-1, -1), 'LD_UU': (-2, -2), 'LD_UUU': (-3, -3)},
    {'LD_D': (1, -1), 'LD_DD': (2, -2), 'LD_DDD': (3, -3)},
    {'RD_U': (-1, 1), 'RD_UU': (-2, 2), 'RD_UUU': (-3, 3)},
    {'RD_D': (1, 1), 'RD_DD': (2, 2), 'RD_DDD': (3, 3)}
]


def choose_col():
    while True:
        choice = int(input(f"{current_player[0]}, please choose a column between [1-7]: "))
        column = choice - 1
        try:
            int(choice)
            if choice < 1 or choice > 7:
                print("Incorrect column. Please choose a column between [1-7]: ")
                continue
        except ValueError:
            print("Invalid column! Please choose a column between [1-7]")
            continue
        else:
            break
    return column


def valid_index(new_row, new_col, brd):
    if new_row < 0 or new_row >= len(brd):
        return False
    if new_col < 0 or new_col >= len(brd[0]):
        return False
    return True


def check_winner(mapper, cur_row, cur_col, brd, cur_player):
    for element in mapper:
        winning_path = 0
        for j, v in element.items():
            new_row = cur_row + v[0]
            new_col = cur_col + v[1]
            valid = valid_index(new_row, new_col, brd)
            if valid and brd[new_row][new_col] == cur_player[1]:
                winning_path += 1
            else:
                break
        if winning_path == 3:
            return True
    return False


player_one_name = input('Player one, please insert your name: ')
player_two_name = input('Player two, please insert your name: ')
player_one = (player_one_name, 1)
player_two = (player_two_name, 2)
board = [[0 for c in range(7)] for r in range(6)]

# play the game:
turns = 1
while True:
    current_player = player_one if turns % 2 != 0 else player_two
    current_row = 0
    current_col = choose_col()

    #play the player turn
    for index in range(5, -1, -1):
        if board[index][current_col] == 0:
            board[index][current_col] = current_player[1]
            turns += 1
            current_row = index
            break
        elif board[0][current_col] != 0:
            print(f"Invalid choice, {current_col} already populated. Choose again!")
            break

    # print board:
    for rr in board:
        print(rr)

    # check if we have a winner.
    if turns >= 7:
        result = check_winner(position_map, current_row, current_col, board, current_player)
        if result:
            print(f'The winner is {current_player[0]}')
            exit()






