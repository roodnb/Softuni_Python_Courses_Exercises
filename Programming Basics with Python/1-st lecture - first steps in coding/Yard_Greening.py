square_meters_for_greening = float(input())
one_square_meter_of_greening = 7.61
price_to_pay = square_meters_for_greening * one_square_meter_of_greening
discount_value = 0.18
discount_for_Bozhidara = price_to_pay * discount_value
total_price_to_pay = price_to_pay - discount_for_Bozhidara


print(f'The final price is: {total_price_to_pay} lv.')
print(f'The discount is {discount_for_Bozhidara} lv.')