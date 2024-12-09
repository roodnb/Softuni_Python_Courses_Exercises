import tkinter

# Дадената функция ще създаде прозорчето на прогррамата.
def create_app():
    root = tkinter.Tk()  #създаваме инстанция, защото реално Tk() е клас. Реално инстанцията това е самия обект.
                         # Реално създаваме обект от клас Tk()
    root.geometry('700x600+0+0')    # създаваме размери на прозорчето,
                                    # 700 хор на 600 вер + началаото на прозореца 0 и 0 - горен ляв ъгъл на екрана.
                                    # това е в пиксели. демек на нулев и нулев пиксел
    root.title("Gui Product Shop") # създаваме име на прозорчето
    return root


app = create_app()  # app realno izvikva funckiqta , koqto vyrshta nqkye obekt root ot class Tk i na kogoto sym prilojil
                    # syotvetnite metodi geometry i title