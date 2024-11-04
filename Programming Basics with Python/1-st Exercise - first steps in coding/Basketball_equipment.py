annual_workout_fee = int(input())

shoes_price = 0.6 * annual_workout_fee
clothes_price = 0.8 * shoes_price
ball_price = 0.25 * clothes_price
accessories = 0.2 * ball_price

sum = annual_workout_fee + shoes_price + clothes_price + ball_price + accessories

print(sum)