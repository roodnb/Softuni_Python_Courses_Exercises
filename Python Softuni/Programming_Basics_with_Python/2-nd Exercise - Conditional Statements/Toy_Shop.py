puzzle_price = 2.60
speaking_doll_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2


fun_price = float(input())
number_puzzles = int(input())
number_doll = int(input())
number_bear = int(input())
number_minion = int(input())
number_truck = int(input())

total_numbers_of_ordered_toys = number_puzzles + number_doll + number_bear + number_minion + number_truck
total_income = number_puzzles*2.60 + number_doll*3 + number_bear*4.10 + number_minion*8.20 + number_truck*2

if total_numbers_of_ordered_toys >= 50:
    total_income *= 0.75

total_income *= 0.9

if total_income >= fun_price: # в задачата се казва дали парите сще стигнат. ами реално и оставащото да е 0 те пак стигат.
    print(f"Yes! {total_income - fun_price:.2f} lv left.")

if total_income < fun_price:
    print(f"Not enough money! {fun_price - total_income:.2f} lv needed.")