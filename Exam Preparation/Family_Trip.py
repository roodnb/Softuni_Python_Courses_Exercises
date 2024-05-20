budget = float(input())
number_of_nights = int(input())
price_per_night = float(input())
percent_additional_cost = int(input())


if number_of_nights > 7:
    price_per_night *= 0.95
    total_price_per_night = price_per_night * number_of_nights
    actual_percent_taken = budget * percent_additional_cost / 100
    total_spend = total_price_per_night + actual_percent_taken
    if total_spend <= budget:
        print(f'Ivanovi will be left with {budget - total_spend:.2f} leva after vacation.')
    else:
        print(f'{total_spend - budget:.2f} leva needed.')
else:
    total_price_per_night = price_per_night * number_of_nights
    actual_percent_taken = budget * percent_additional_cost / 100
    total_spend = total_price_per_night + actual_percent_taken
    if total_spend <= budget:
        print(f'Ivanovi will be left with {budget - total_spend:.2f} leva after vacation.')
    else:
        print(f'{total_spend - budget:.2f} leva needed.')




