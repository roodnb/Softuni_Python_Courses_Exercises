import sys
number_of_films = int(input())

highest_rating = -sys.maxsize
lowest_rating = sys.maxsize
highest_film = ''
lowest_film = ''
average_rating = 0

while True:
    for i in range(number_of_films):
        name_of_film = input()
        rating = float(input())
        if rating > highest_rating:
            highest_rating = rating
            highest_film = name_of_film

        elif rating < lowest_rating:
            lowest_rating = rating
            lowest_film = name_of_film

        average_rating += rating

    print(f'{highest_film} is with highest rating: {highest_rating:.1f}')
    print(f'{lowest_film} is with lowest rating: {lowest_rating:.1f}')
    print(f'Average rating: {average_rating / number_of_films:.1f}')
    break
