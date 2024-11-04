name = input()
grades_total = 0
years_counter = 0
excluded = 0
while True:
    annual_grade = float(input())

    if annual_grade < 4:
        excluded += 1
        if excluded == 2:
            print(f'{name} has been excluded at {years_counter + 1} grade')
            break
        continue
    grades_total += annual_grade
    years_counter += 1
    if years_counter == 12:
        avarage_grade = grades_total / 12
        print(f'{name} graduated. Average grade: {avarage_grade:.2f}')