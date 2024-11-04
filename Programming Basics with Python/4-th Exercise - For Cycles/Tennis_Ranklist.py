tournaments = int(input())
starting_balance = int(input())


total_points = starting_balance
wins = 0

for games in range(tournaments):
    position = str(input())
    if position == 'W':
        total_points += 2000
        wins += 1
    elif position == 'F':
        total_points += 1200
    elif position == 'SF':
        total_points += 720

from math import floor
average_points = floor((total_points - starting_balance)/tournaments)


print(f'Final points: {total_points}')
print(f'Average points: {average_points}')
print(f'{(wins/tournaments)*100:.2f}%')