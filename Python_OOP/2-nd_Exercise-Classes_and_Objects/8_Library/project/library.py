from project.user import User


class Library:
    def __init__(self):
        self.user_records: list[User] = []
        self.books_available: dict[str, list[str]] = {}  # authors (key: str) and the books available for each of them (list of strings)
        self.rented_books: dict[str, dict[str, int]] = {}  # {usernames: {book names: days to return}}.

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if author in self.books_available and book_name in self.books_available[author]:
            user.books.append(book_name)
            self.books_available[author].remove(book_name)
            if user.username not in self.rented_books:
                self.rented_books[user.username] = {}
            self.rented_books[user.username][book_name] = days_to_return
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        else:
            for username, books_data in self.rented_books.items():
                if book_name in self.rented_books[username]:
                    return (f'The book "{book_name}" is already rented and will be available in '
                            f'{books_data[book_name]} days!')

    def return_book(self, author:str, book_name:str, user: User):
        if book_name in user.books:
            user.books.remove(book_name)
            del self.rented_books[user.username][book_name]
            self.books_available[author].append(book_name)
        return f"{user.username} doesn't have this book in his/her records!"