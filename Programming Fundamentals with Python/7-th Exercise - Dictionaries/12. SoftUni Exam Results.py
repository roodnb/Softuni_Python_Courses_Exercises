exam_results = {}
courses_dictionary = {}

while True:
    command = input()

    if command == 'exam finished':
        break

    current_command = command.split('-')
    student_name = current_command[0]

    if current_command[1] == 'banned':
        del exam_results[student_name]
        continue

    course = current_command[1]
    points = int(current_command[2])

    if student_name not in exam_results.keys():
        exam_results[student_name] = 0
    if exam_results[student_name] < points:
        exam_results[student_name] = points
    if course not in courses_dictionary.keys():
        courses_dictionary[course] = 0
    courses_dictionary[course] += 1

print('Results:')
for name, max_points in exam_results.items():
    print(f"{name} | {max_points}")
print("Submissions:")
for course, number_of_students in courses_dictionary.items():
    print(f"{course} - {number_of_students}")