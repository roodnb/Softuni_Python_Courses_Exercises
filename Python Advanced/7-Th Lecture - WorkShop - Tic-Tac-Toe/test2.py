import tkinter as tk
from tkinter import messagebox
from functools import partial

SIZE = 3

app_config: dict = {'board': [[None] * SIZE for _ in range(SIZE)],
                    'buttons': [[None] * SIZE for _ in range(SIZE)],
                    'sign': None,
                    'X': None,
                    '0': None}


def is_win_rows(board_):
    for r in board_:
        if len(set(r)) == 1 and r[0] is not None:
            return True
    return False


def is_win_cols(board_, curr_sign):
    for c in range(len(board_)):
        current_col = []
        for r in range(len(board_)):
            current_col.append(board_[r][c] == curr_sign)
        if all(current_col):
            return True
    return False


def is_win_diagonals(board_, curr_sign):
    diagonal_1, diagonal_2 = [], []
    for idx in range(len(board_)):
        diagonal_1.append(board_[idx][idx] == curr_sign)
        diagonal_2.append(board_[idx][len(board_) - 1 - idx] == curr_sign)
    return all(diagonal_1) or all(diagonal_2)


def is_win(board_, curr_sign):
    return any([is_win_rows(board_), is_win_cols(board_, curr_sign), is_win_diagonals(board_, curr_sign)])


def is_win_row_possible(board_):
    return not all(['X' in r and '0' in r for r in board_])


def is_win_col_possible(board_):
    columns = []  # True, True, True
    for c in range(len(board_)):
        current_col = [board_[r][c] for r in range(len(board_))]
        columns.append('X' in current_col and '0' in current_col)
    return not all(columns)


def is_win_diagonal_possible(board_):
    diagonal_1, diagonal_2 = [], []
    for idx in range(len(board_)):
        diagonal_1.append(board_[idx][idx])
        diagonal_2.append(board_[idx][len(board_) - 1 - idx])
    if 'X' in diagonal_1 and '0' in diagonal_1 and 'X' in diagonal_2 and '0' in diagonal_2:
        return False
    return True


def is_draw(board_):
    return not any([is_win_row_possible(board_), is_win_col_possible(board_), is_win_diagonal_possible(board_)])


def get_content(row, col, window):
    if app_config['board'][row][col] is None:
        app_config['board'][row][col] = app_config['sign']
        app_config['buttons'][row][col].config(text=app_config['board'][row][col])
        if is_win(app_config['board'], app_config['sign']):
            window.destroy()
            messagebox.showinfo("Winner", f"Player {app_config[app_config['sign']]} wins!")
        elif is_draw(app_config['board']):
            window.destroy()
            messagebox.showinfo("Draw", "The game ended in a draw!")
        app_config['sign'] = 'X' if app_config['sign'] == '0' else '0'


def render_board(window):
    grid_frame = tk.Frame(master=window)
    grid_frame.pack(padx=10, pady=10)
    for row in range(SIZE):
        for col in range(SIZE):
            gc = partial(get_content, row, col, window)
            app_config['buttons'][row][col] = tk.Button(
                master=grid_frame,
                command=gc,
                text=app_config['board'][row][col] if app_config['board'][row][col] else ' ',
                width=5,
                height=2
            )
            app_config['buttons'][row][col].grid(row=row, column=col)


def start_game(window, player_one, player_two, player_one_sign, player_two_sign):
    window.destroy()
    window = tk.Tk()
    window.geometry('240x240')
    window.title('Tic Tac Toe')

    app_config['sign'] = player_one_sign
    app_config[player_one_sign] = player_one
    app_config[player_two_sign] = player_two

    p1 = tk.Label(window, text=f'{player_one} plays with {player_one_sign}', width=20)
    p2 = tk.Label(window, text=f'{player_two} plays with {player_two_sign}', width=20)
    p1.pack()
    p2.pack()

    render_board(window)


def start_screen():
    window = tk.Tk()
    window.geometry('240x240')
    window.title('Tic Tac Toe')

    tk.Label(window, text='First player name: ').pack()
    player_one = tk.Entry(window)
    player_one.pack()
    p_one_sign = tk.StringVar()
    p_one_sign.set('X')
    tk.Label(window, text='Choose sign for first player:').pack()
    tk.Radiobutton(window, text='X', variable=p_one_sign, value='X').pack()
    tk.Radiobutton(window, text='0', variable=p_one_sign, value='0').pack()
    tk.Label(window, text='Second player name: ').pack()
    player_two = tk.Entry(window)
    player_two.pack()

    tk.Button(window,
              text='Start game',
              command=lambda: start_game(window,
                                         player_one.get(),
                                         player_two.get(),
                                         p_one_sign.get(),
                                         'X' if p_one_sign.get() == '0' else '0')
              ).pack()

    window.mainloop()


if __name__ == '__main__':
    start_screen()