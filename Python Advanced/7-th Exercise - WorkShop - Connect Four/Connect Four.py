#Position mapper
position_map = [
    {'D': (1, 0), 'DD': (2, 0), 'DDD': (3, 0)},
    {'L': (0, -1), 'LL': (0, -2), 'LLL': (0, -3)},
    {'R': (0, 1), 'RR': (0, 2), 'RRR': (0, 3)},
    {'LD_U': (-1, -1), 'LD_UU': (-2, -2), 'LD_UUU': (-3, -3)},
    {'LD_D': (1, -1), 'LD_DD': (2, -2), 'LD_DDD': (3, -3)},
    {'RD_U': (-1, 1), 'RD_UU': (-2, 2), 'RD_UUU': (-3, 3)},
    {'RD_D': (1, 1), 'RD_DD': (2, 2), 'RD_DDD': (3, 3)}
]

player_one_name = input('Player one, please insert your name: ')
player_two_name = input('Player two, please insert your name: ')
player_one = (player_one_name, 1)
player_two = (player_two_name, 2)
#creating the board
board = [[0 for c in range(7)] for r in range(6)]


# play the game:
turns = 1
while True:
    current_player = player_one if turns % 2 != 0 else player_two
    chosen_col = int(input(f"{current_player[0]}, please choose a column: ")) - 1

    current_row = 0
    current_col = chosen_col

    ### place the position in the board and check if we dont go above the board - board[0].
    for index in range(5, -1, -1):
        if board[index][chosen_col] == 0:
            board[index][chosen_col] = current_player[1]
            turns += 1
            current_row = index
            break

        elif board[0][chosen_col] != 0:
            print(f"Invalid choice, {chosen_col} already populated. Choose again!")
            break

    ###print board:
    for rr in board:
        print(rr)

    ### check if we have a winner.
    if turns > 7:
        for element in position_map:
            winning_path = 0
            for j, v in element.items():
                new_row = current_row + v[0]
                new_col = current_col + v[1]
                if new_row < 0 or new_row >= len(board) or new_col < 0 or new_col >= len(board[0]):
                    continue
                else:
                    if board[new_row][new_col] == current_player[1]:
                        winning_path += 1

            if winning_path == 3:
                print(f'The winner is {current_player[0]}')
                exit()







