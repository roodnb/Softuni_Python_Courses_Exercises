daily_allowance = float(input())
daily_profit = float(input())
money_spend = float(input())
gift_price = float(input())


number_of_days_till_bday = 5

total_daily_saved = daily_allowance * 5
total_daily_profit = daily_profit * 5
total_saved = total_daily_saved + total_daily_profit

total_spend = total_saved - money_spend

if total_spend >= gift_price:
    print(f'Profit: {total_spend:.2f} BGN, the gift has been purchased.')

else:
    print(f'Insufficient money: {gift_price - total_spend:.2f} BGN.')