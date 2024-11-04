from math import floor

number_of_pages = int(input())
pages_per_hour = int(input())
number_of_days_to_read_the_book = int(input())

hours_needed = floor(number_of_pages / pages_per_hour)
number_of_days = int(hours_needed / number_of_days_to_read_the_book)

print(number_of_days)





# read_hours_per_day = (pages_in_book / pages_per_hour) / days_per_book
# print(floor(read_hours_per_day))