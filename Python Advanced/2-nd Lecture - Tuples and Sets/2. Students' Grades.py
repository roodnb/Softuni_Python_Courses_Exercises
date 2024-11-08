number_of_students = int(input())

student_data = {}

for _ in range(number_of_students):
    student, grade = input().split(' ')
    if student not in student_data:
        student_data[student] = []
    student_data[student].append(float(grade))


for k, v in student_data.items():
    avg_grade = sum(v) / len(v)
    print(f"{k} -> {' '.join([f'{el:.2f}' for el in v])} (avg: {avg_grade:.2f})")
