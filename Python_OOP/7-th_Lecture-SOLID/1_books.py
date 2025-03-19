class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self):
        self.books: list[Book] = []

    def add_book(self, book: "Book"):
        self.books.append(book)

    def find_book(self, title):
        book_to_find = [b for b in self.books if b.title == title][0]
        return book_to_find
