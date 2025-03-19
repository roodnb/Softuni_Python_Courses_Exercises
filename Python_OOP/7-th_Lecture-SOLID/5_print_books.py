from abc import ABC, abstractmethod


class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter(ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        pass


class A4Formatter(Formatter):

    def format(self, book: Book) -> str:
        return "formatted boot to A4"


class PaperFormatter(Formatter):
    def format(self, book: Book) -> str:
        return "paper formatted"


class Printer:
    @staticmethod
    def get_book(formatter: Formatter, book: Book):
        formatted_book = formatter.format(book)
        return formatted_book


book = Book('test')
p = PaperFormatter()
prt = Printer()

print(prt.get_book(p, book))
