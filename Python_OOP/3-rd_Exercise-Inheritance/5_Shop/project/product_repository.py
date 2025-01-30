from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: list[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        try:
            product_to_find = [el for el in self.products if el.name == product_name][0]
            return product_to_find
        except IndexError:
            pass

    def remove(self, product_name: str):
        try:
            product = [el for el in self.products if el.name == product_name][0]
            self.products.remove(product)
        except IndexError:
            pass

    def __repr__(self):
        return "\n".join([f"{ele.name}: {ele.quantity}" for ele in self.products])