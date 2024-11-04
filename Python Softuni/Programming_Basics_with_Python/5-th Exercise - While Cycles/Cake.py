width = int(input())
length = int(input())

number_of_pieces = width * length
pieces_requested = 0

while number_of_pieces >= 0:
    command = input()
    if command == 'STOP':
        print(f'{abs(number_of_pieces)} pieces are left.')
        break
    pieces_taken = int(command)
    number_of_pieces -= pieces_taken
    pieces_requested += pieces_taken
    if number_of_pieces < 0:
        print(f'No more cake left! You need {abs(number_of_pieces)} pieces more.')
        break
