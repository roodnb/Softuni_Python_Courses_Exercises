if type_of_room == 'apartment':
    if days_of_stay < 0:
        money_spend = (nights_of_stay * 25) * 0.70
    elif 10 <= days_of_stay <= 15:
        money_spend = (nights_of_stay * 25) * 0.65
    elif days_of_stay > 15:
        money_spend = (nights_of_stay * 25) * 0.5
        if grade == 'positive':
            money_spend *= 1.25
        elif grade == 'negative':
            money_spend *= 0.9



if grade is