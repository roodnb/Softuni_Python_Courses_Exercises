book = input()

book_counter = 0


while True:
    new_book = input()
    if new_book == book:
        print(f'You checked {book_counter} books and found it.')
        break
    if new_book == 'No More Books':
        print('The book you search is not here!')
        print(f'You checked {book_counter} books.')
        break
    book_counter += 1


'''
drugo reshenie

book_name = input()

book_count = 0
is_book_found = False

current_book = input()

while current_book != 'No More Books':
    if current_book == book_name:
        is_book_found = True
        print(f'You checked {book_count} books and found it.')
        break

    book_count += 1
    current_book = input()

if not is_book_found:
    print('The book you search is not here!')
    print(f'You checked {book_count} books.')


'''