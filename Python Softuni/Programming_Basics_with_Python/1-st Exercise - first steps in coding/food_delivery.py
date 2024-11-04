chicken_menu_price = 10.35
fish_menu_price = 12.40
veggie_menu_price = 8.15


number_of_chicken_menu = int(input())
number_of_fish_menu = int(input())
number_of_veggie_menu = int(input())

total_ordered_chicken_menu_price = number_of_chicken_menu * chicken_menu_price
total_ordered_fish_menu_price = number_of_fish_menu * fish_menu_price
total_ordered_veggie_menu_price = number_of_veggie_menu * veggie_menu_price
desert_price = 0.2 * (total_ordered_veggie_menu_price + total_ordered_fish_menu_price + total_ordered_chicken_menu_price)
deliver_price = 2.50


total_sum = total_ordered_chicken_menu_price + total_ordered_fish_menu_price + total_ordered_veggie_menu_price + desert_price + deliver_price

print(total_sum)