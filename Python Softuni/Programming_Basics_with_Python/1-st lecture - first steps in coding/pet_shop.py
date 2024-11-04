number_of_dog_food_package = int(input())
number_of_cat_food_package = int(input())
dog_food_package_price = float(2.50)
cat_food_package_price = float(4)
dog_food_sold = dog_food_package_price * number_of_dog_food_package
cat_food_sold = cat_food_package_price * number_of_cat_food_package
sum = dog_food_sold + cat_food_sold

print(sum, '.lv')

# OR
# print(f'{sum} lv.')