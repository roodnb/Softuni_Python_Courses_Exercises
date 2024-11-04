film_name = input()
number_of_days = int(input())
number_of_tickets = int(input())
price = float(input())
percent_for_cinema = int(input())


daily_profit = number_of_tickets * price
total_profit = daily_profit * number_of_days
total_percent_taken = total_profit * percent_for_cinema / 100
remaining_profit = total_profit - total_percent_taken

print(f'The profit from the movie {film_name} is {remaining_profit:.2f} lv.')