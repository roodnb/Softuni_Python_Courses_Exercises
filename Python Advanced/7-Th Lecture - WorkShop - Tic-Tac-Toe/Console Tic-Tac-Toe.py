from math import ceil
# from random import randint


def setup():
    global player_one, player_two
    player_one_name = input("Player one name: ")
    player_two_name = input("Player two name: ")
    while True:
        player_one_sign = input(f'{player_one_name} would you like to play with "X" or "O"?: ')
        if player_one_sign.upper() in ('X', "O"):
            break
        else:
            print("Invalid sign. Choose again!")
    player_two_sign = 'X' if player_one_sign == 'O' else "O"
    player_one = [player_one_name, player_one_sign]
    player_two = [player_two_name, player_two_sign]
    print("This is the numeration of the board:")
    print("|  1  |  2  |  3  |")
    print("|  4  |  5  |  6  |")
    print("|  7  |  8  |  9  |")
    print(f"{player_one_name} starts first!")


def draw_board(current_board):
    for row in current_board:
        print(f'|  {"  |  ".join([str(el) for el in row])}  |')


def check_if_won(current_player, current_board):
    global loop
    first_row = all(x == current_player[1] for x in current_board[0])
    second_row = all(x == current_player[1] for x in current_board[1])
    third_row = all(x == current_player[1] for x in current_board[2])
    first_col = all(x == current_player[1] for x in [current_board[0][0], current_board[1][0], current_board[2][0]])
    second_col = all(x == current_player[1] for x in [current_board[0][1], current_board[1][1], current_board[2][2]])
    third_col = all(x == current_player[1] for x in [current_board[0][2], current_board[1][2], current_board[2][2]])
    first_diag = all(x == current_player[1] for x in [current_board[0][0], current_board[1][1], current_board[2][2]])
    second_diag = all(x == current_player[1] for x in [current_board[2][0], current_board[1][1], current_board[0][2]])
    if any([first_row, second_row, third_row, first_col, second_col, third_col, first_diag, second_diag]):
        print(f"{current_player[0]} won!")
        loop = False


def play(current_player, current_board):
    row = 0
    col = 0
    while True:
        # if current_player == player_two:
        #     choice = f'{current_player[0]} choose a free position [1-9]: {randint(1, 9)}'
        # else:
        choice = int(input(f"{current_player[0]} choose a free position [1-9]: "))
        if choice < 1 or choice > 9:
            print('Incorrect position. The position must be between [1-9]!')
            continue
        row = ceil(choice / 3) - 1
        col = choice % 3 - 1
        ''' na row se polzwa ceil zahtoto :
        1-vo matricata indeksite sa 0/1/2 dokato na dyskata sa 1/2/3 i respektivno kato pylnim go prabvim ot index 0
        za row - naprimer 1 / 3 = 0.33 , 2 / 3  = 0.66. sys ceil go zakryglqme do 1. obache index ot 1 e red 2 a ne
        pyrviq red , za towa vadim 1. tuk ne polzvame modulnoto delenie ZASHTOTO na pyrviq red imam 1, 2, 3. koito ako 
        delim s modulno delenie 1 % 2 = 1, 2%3 = 2 , 3%3 = 0
        respektivno pri kolonite polzvame modulno delenie zashtoto pri kolonite imam 1, 4, 7 
        i te veche razdeleni na % - 1 davat samata koolna
        '''

        current_board[row][col] = current_player[1]
        draw_board(current_board)
        check_if_won(current_player, current_board)


player_one = None
player_two = None
board = [['', '', ''], ['', '', ''], ['', '', '']]
setup()
current = player_one
other = player_two
loop = True


while loop:
    play(current, board)
    current, other = other, current
