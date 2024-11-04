number_of_rows = int(input())
students = {}
for student_grade in range(number_of_rows):
    student = input()
    grade = float(input())
    if student not in students.keys():
        students[student] = [0, 0] # [student grade, student name count]
        students[student][0] += grade
        students[student][1] += 1
    else:
        students[student][0] += grade
        students[student][1] += 1

for key,value in students.items():
    average = value[0] / value[1]
    if average>= 4.50:
        print(f'{key} -> {average:.2f}')

