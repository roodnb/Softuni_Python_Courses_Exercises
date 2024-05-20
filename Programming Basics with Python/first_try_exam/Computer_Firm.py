number = int(input())
possible_sales = 0
sales = 0
rating = 0
count_of_rating = 0
for i in range(number):
    number_possible_sales_and_rating = input()
    rating = int(number_possible_sales_and_rating[-1])
    count_of_rating += rating
    possible_sales = int(number_possible_sales_and_rating) // 10
    if rating == 2:
        sales += possible_sales * 0
    elif rating == 3:
        sales += possible_sales * 0.5
    elif rating == 4:
        sales += possible_sales * 0.7
    elif rating == 5:
        sales += possible_sales * 0.85
    elif rating == 6:
        sales += possible_sales * 1
print(f'{sales:.2f}')
print(f'{count_of_rating / number:.2f}')