command = input()
course_dict = {}

while command != 'end':
    course, student = command.split(' : ')
    if course not in course_dict.keys():
        course_dict[course] = {}
        course_dict[course]['number_of_students'] = 0
        course_dict[course]['students'] = []

    if student not in course_dict[course]['students']:
        course_dict[course]['students'].append(student)
    course_dict[course]['number_of_students'] += 1
    command = input()
print(course_dict)
# for key,value in course_dict.items():
#     print(f'{key}: {value[0]}')
#     for index in range(len(value) -1):
#         print(f'-- {value[index + 1]}')




# command = input()
# course_dict = {}
#
# while command != 'end':
#     course, student = command.split(' : ')
#     if course not in course_dict.keys():
#         course_dict[course] = []
#         course_dict[course].append(0)
#     if student not in course_dict.values():
#         course_dict[course].append(student)
#     course_dict[course][0] += 1
#     command = input()
#
# for key,value in course_dict.items():
#     print(f'{key}: {value[0]}')
#     for index in range(len(value) -1):
#         print(f'-- {value[index + 1]}')