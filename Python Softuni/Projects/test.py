import random

player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

if player_move == 'r':
    player_move = 'Rock'
elif player_move == 'p':
    player_move = 'Paper'
elif player_move == 's':
    player_move = 'Scissors'
else:
    raise SystemExit("Invalid Input. Try again...")

computer_random_number = random.randint(1, 3)
computer_move = ''

if computer_random_number == 1:
    computer_move = 'Rock'
elif computer_random_number == 2:
    computer_move = 'Paper'
else:
    computer_move = 'Scissors'
print(f"The computer chose {computer_move}")

if (player_move == 'r' and computer_move == 's') or \
        (player_move == 'p' and computer_move == 'r') or \
        (player_move == 's'and computer_move == 'p'):
    print('You win!')
elif player_move == computer_move:
    print('Draw!')
else:
    print('You lose!')

