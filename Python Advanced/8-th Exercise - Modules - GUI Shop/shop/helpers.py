import tkinter
from canvas import app


def clean_screen():
    for element in app.grid_slaves(): # slaves sa dyshternite elementi zakacheni kym v nashiq sluchai kym obekta app
        element.destroy()


def exit_button():
    tkinter.Button(app,
                   text='Exit',
                   bg='green',
                   fg='black',
                   command=app.destroy
                   ).grid(row=100, column=0, pady=10)

