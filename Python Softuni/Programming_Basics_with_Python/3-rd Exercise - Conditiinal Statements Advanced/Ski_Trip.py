days_of_stay = int(input())
type_of_room = str(input())
grade = str(input())

nights_of_stay = days_of_stay - 1

money_spend = 0
discount = 0
premium = 0


if type_of_room == 'room for one person':
    money_spend = nights_of_stay * 18
    if grade == 'positive':
        money_spend *= 1.25
    elif grade == 'negative':
        money_spend *= 0.9
    print(f'{money_spend:.2f}')
    exit()

if type_of_room == 'apartment':
    if days_of_stay < 10:
        money_spend = (nights_of_stay * 25) * 0.70
    elif 10 <= days_of_stay <= 15:
        money_spend = (nights_of_stay * 25) * 0.65
    elif days_of_stay > 15:
        money_spend = (nights_of_stay * 25) * 0.5



if type_of_room == 'president apartment':
    if days_of_stay < 10:
        money_spend = (nights_of_stay * 35) * 0.9
    elif 10 <= days_of_stay <= 15:
        money_spend = (nights_of_stay * 35) * 0.85
    elif days_of_stay > 15:
        money_spend = (nights_of_stay * 35) * 0.8


if grade == 'positive':
    money_spend *= 1.25
elif grade == 'negative':
    money_spend *= 0.9

print(f'{money_spend:.2f}')