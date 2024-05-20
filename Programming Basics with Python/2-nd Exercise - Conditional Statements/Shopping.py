peters_budget = float(input())
video_card_number = int(input())
cpu_numer = int(input())
ram_number = int(input())

video_card_single_price = 250
video_card_price = 250 * video_card_number
cpu_price = (video_card_number * video_card_single_price) * 0.35 * cpu_numer
ram_price = (video_card_number * video_card_single_price) * 0.1 * ram_number

total_price = video_card_price + cpu_price + ram_price

if video_card_number > cpu_numer:
    total_price *= 0.85

if peters_budget >= total_price:
    print(f'You have {peters_budget - total_price:.2f} leva left!')

if peters_budget < total_price:
    print(f'Not enough money! You need {total_price - peters_budget:.2f} leva more!')