import tkinter
import json
from canvas import app
from helpers import clean_screen, exit_button
from products import render_product_screen


def login(user, passw):
    with open('C:\\Users\\B58943644\\PycharmProjects\\Softuni_Python_Courses_Exercises'
              '\\Python Advanced\\8-th Exercise - Modules - GUI Shop'
              '\\shop\\db\\user_credentials_db.txt') as file:
        data = file.readlines()
        for line in data:
            n, p = line.strip().split(', ')
            if user == n and passw == p:
                with open('C:\\Users\\B58943644\\PycharmProjects\\Softuni_Python_Courses_Exercises'
                          '\\Python Advanced\\8-th Exercise - Modules - GUI Shop'
                          '\\shop\\db\\current_user.txt', 'w') as f:
                    f.write(n)
                render_product_screen()
                return

    render_login_screen(error_msg="Invalid username or password!")


def register(**kwargs):
    # TODO: Validations
    kwargs.update({"procedure": []})
    with open('C:\\Users\\B58943644\\PycharmProjects\\Softuni_Python_Courses_Exercises'
              '\\Python Advanced\\8-th Exercise - Modules - GUI Shop'
              '\\shop\\db\\user_credentials_db.txt', "r+", newline="\n") as file:  #r+ shtoto shte chetem i pishem
        users = [line.strip().split(', ')[0] for line in file]  # izcheti veski 1 red, mahni \n ot wseki red ( tam e no
                                                                # no ne se wijda), sled koeto splitni po zapetaq i wzemi tva na index 0
        if kwargs["username"] in users:
            render_register_screen(error_msg="User already exists")
            return
        file.write(f"{kwargs['username']}, {kwargs['password']}")

    with open('C:\\Users\\B58943644\\PycharmProjects\\Softuni_Python_Courses_Exercises'
              '\\Python Advanced\\8-th Exercise - Modules - GUI Shop'
              '\\shop\\db\\users.txt', 'a', newline='\n') as f:

        f.write(json.dumps(kwargs))
        f.write('\n')
    render_login_screen()


def render_login_screen(error_msg=None):
    clean_screen()
    username = tkinter.Entry(app)
    username.grid(row=0, column=0)
    password = tkinter.Entry(app, show='*')
    password.grid(row=1, column=0)

    if error_msg:
        tkinter.Label(app, text=error_msg).grid(row=3, column=0)

    tkinter.Button(app,
                   text='Enter',
                   bg='green',
                   fg='black',
                   command=lambda: login(username.get(), password.get())
                   ).grid(row=2, column=0)
    exit_button()


def render_register_screen(error_msg=None):
    clean_screen()
    username = tkinter.Entry(app)
    username.grid(row=0, column=0)
    password = tkinter.Entry(app, show='*')
    password.grid(row=1, column=0)
    first_name = tkinter.Entry(app)
    first_name.grid(row=2, column=0)
    last_name = tkinter.Entry(app)
    last_name.grid(row=3, column=0)

    tkinter.Button(app,
                   text='Register',
                   bg='green',
                   fg='black',
                   command=lambda: register(
                       username=username.get(),
                       password=password.get(),
                       first_name=first_name.get(),
                       last_name=last_name.get())
                   ).grid(row=4, column=0)
    exit_button()
    if error_msg:
        tkinter.Label(app, text=error_msg).grid(row=5, column=0)


def render_main_enter_screen():
    tkinter.Button(app,
                   text='Login',
                   bg='green', #background - button color
                   fg='white', #forground = text color
                   command= render_login_screen
                   ).grid(row=0, column=0)

    tkinter.Button(app,
                   text='Register',
                   bg='yellow',  # background - button color
                   fg='black', # forground = text color
                   command=render_register_screen # puskame referenciq kym funkciqta NO ne q izwikvame
                   ).grid(row=0, column=1)

    exit_button()

