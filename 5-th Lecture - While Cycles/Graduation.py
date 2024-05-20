name = input()

class_counter = 0
sum_grades = 0
exclude = 0

while class_counter <= 12:
    grade = float(input())
    if grade < 4:
        exclude += 1
        if exclude == 2:
            print(f'{name} has been excluded at {class_counter + 1} grade')
            break
        continue

    sum_grades += grade
    class_counter += 1

    if class_counter == 12:
        avarage = sum_grades / 12
        print(f'{name} graduated. Average grade: {avarage:.2f}')
        break



'''
druga opciq

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
        break


'''


