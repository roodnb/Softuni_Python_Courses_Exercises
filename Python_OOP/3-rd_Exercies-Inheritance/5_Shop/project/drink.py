from project.product import Product


class Drink(Product):
    '''
    # variant 1 kato pri tozi variant quantity defaultno shte vzeme 10 no moje da byde promeneno.
    def __init__(self, name: str, quantity = 10):
        super().__init__(name, quantity)
    '''
    # variant 2 pri tozi variant quantity e 10 voveki.
    def __init__(self, name: str):
        super().__init__(name, 10)

