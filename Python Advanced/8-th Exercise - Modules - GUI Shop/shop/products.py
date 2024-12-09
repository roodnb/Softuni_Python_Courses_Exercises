import json
import tkinter
from helpers import clean_screen, exit_button
from canvas import app
import os
from PIL import Image, ImageTk


base_folder = os.path.dirname(__file__)
'''
tozi pyt shte ni trqbva posle za path-a do vseki 1 immage.
w sluchaq s gornoto os.path.dirname(__file__) kazvame nameri i zapishi v promenlivata base_folder, 
path-a kym tekushtiq file products.py
'''


def update_current_user(username, product_id):
    with open('C:\\Users\\B58943644\\PycharmProjects\\Softuni_Python_Courses_Exercises\\Python Advanced\\8-th Exercise - Modules - GUI Shop\\shop\\db\\users.txt', 'r+', newline='\n') as file:
        users = [json.loads(u.strip()) for u in file]
        for usr in users:
            if usr['username'] == username:
                usr['products'].append(product_id)
                file.seek(0)
                file.truncate()
                file.writelines(json.dumps(u) + '\n' for u in users)
                '''Kakvo napravihme tuk:
                nie hubabo izchetohme file-a updatenahme na nashia user infoto no sega trqbva da go zapishem
                obratno v toq file. Obache s gornite deistviq realno file-a ne znae nie koi red user i tn sme pipali.
                za celta iztrivame vsichko i go prenapisvame otnovo s veche updatenatata informacia.'''
                return


def update_products(product_id):
    with open('C:\\Users\\B58943644\\PycharmProjects\\Softuni_Python_Courses_Exercises'
              '\\Python Advanced\\8-th Exercise - Modules - GUI Shop'
              '\\shop\\db\\products.txt', "r+") as file:

        products = [json.loads(prd.strip()) for prd in file]
        for product in products:
            if product_id == product['id']:
                #TODO: check if value is zero
                product['count'] -= 1
                file.seek(0)
                file.truncate()
                file.writelines(json.dumps(p) + '\n' for p in products)
                return


def buy_product(product_id):
    clean_screen()
    with open('C:\\Users\\B58943644\\PycharmProjects\\Softuni_Python_Courses_Exercises'
              '\\Python Advanced\\8-th Exercise - Modules - GUI Shop'
              '\\shop\\db\\current_user.txt',) as file:
        username = file.read()
    if username:
        update_current_user(username, product_id)
        update_products(product_id)
    render_product_screen()


def render_product_screen():
    clean_screen()
    exit_button()

    with open('C:\\Users\\B58943644\\PycharmProjects\\Softuni_Python_Courses_Exercises'
              '\\Python Advanced\\8-th Exercise - Modules - GUI Shop'
              '\\shop\\db\\products.txt') as file:
        # print(file)
        products = [json.loads(p.strip()) for p in file] # изчитаме квото има в Products.txt със стрип махаме \n го набиваме в 1 лист
                                                         # резултата е лист от речниците, който са във Producst.txt
        # print(products)
        products_per_line = 6
        rows_for_product = len(products[0])
        for index, prdct in enumerate(products):

            '''tuk da se obyrne vnimanie za row i col.
            pri row delim celochisleno zashtoto naprimer 7//4 e 1 i go umnojavame po redovete za product = 4
            (Da ne se zabravq che pochvame ot 0)
            pri col delic modylno zashtoto realno tyrsim ostatyka '''
            row = index // products_per_line * rows_for_product
            col = index % products_per_line

            tkinter.Label(app, text=prdct["name"]).grid(row=row, column=col)

            img = Image.open(os.path.join(base_folder, "db\\images", prdct["img_path"])).resize((100, 100))
            photo_image = ImageTk.PhotoImage(img)
            image_label = tkinter.Label(image=photo_image)
            image_label.image = photo_image #bez tova nqma da se poqvi kartinkata.
            image_label.grid(row=row+1, column=col)

            tkinter.Label(app, text=prdct['count']).grid(row=row+2, column=col)

            tkinter.Button(app,
                           text=f'Buy {prdct['id']}',
                           command=lambda pid=prdct["id"]: buy_product(pid)
                           ).grid(row=row+3, column=col)