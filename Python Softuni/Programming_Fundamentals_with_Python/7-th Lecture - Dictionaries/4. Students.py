command = input()
students_data_base = {}
students = []
course_to_search = ''

while True:

    if ':' not in command:
        course_to_search = command
        break

    name, _id, course = command.split(':')
    students.append({'name': name, '_id': _id, 'course': course})
    command = input()

for student in students:
    if course_to_search[:3] in student['course']:
        print(f"{student['name']} - {student['_id']}")
