first_employee_students_per_hour = int(input())
second_employee_students_per_hour = int(input())
third_employee_students_per_hour = int(input())
student_count = int(input())
for_one_hour = first_employee_students_per_hour \
               + second_employee_students_per_hour \
               + third_employee_students_per_hour
total_hours = 0
current_hour = 0
while student_count > 0:
    current_hour += 1
    if current_hour % 4 == 0:
        total_hours += 1
        continue
    student_count -= for_one_hour
    total_hours += 1

print(f'Time needed: {total_hours}h.')