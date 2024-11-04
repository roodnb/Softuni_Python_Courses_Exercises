def _add(init_schedule, lesson_type):
    if lesson_type not in init_schedule:
        init_schedule.append(lesson_type)


def _insert(init_schedule, index_to_put_the_lesson, lesson_type):
    if lesson_type not in init_schedule:
        init_schedule.insert(index_to_put_the_lesson, lesson_type)


def _remove(init_schedule, lesson_type):
    if lesson_type in init_schedule:
        init_schedule.remove(lesson_type)
        exercise_title = lesson_type + '-Exercise'
        if exercise_title in init_schedule:
            init_schedule.remove(exercise_title)


def _swap(init_schedule, lesson_to_be_swapped_with_lesson_type, lesson_type):
    if lesson_type in init_schedule and lesson_to_be_swapped_with_lesson_type in init_schedule:
        index1, index2 = init_schedule.index(lesson_type), init_schedule.index(lesson_to_be_swapped_with_lesson_type)
        init_schedule[index1], init_schedule[index2] = init_schedule[index2], init_schedule[index1]

        exercise1, exercise2 = lesson_type + '-Exercise', lesson_to_be_swapped_with_lesson_type + '-Exercise'
        if exercise1 in init_schedule:
            init_schedule.remove(exercise1)
            init_schedule.insert(init_schedule.index(lesson_type) + 1, exercise1)

        if exercise2 in init_schedule:
            init_schedule.remove(exercise2)
            init_schedule.insert(init_schedule.index(lesson_to_be_swapped_with_lesson_type) + 1, exercise2)


def _exercise(init_schedule, lesson_type):
    exercise_title = lesson_type + '-Exercise'
    if lesson_type in init_schedule:
        lesson_index = init_schedule.index(lesson_type)
        if exercise_title not in init_schedule:
            init_schedule.insert(lesson_index + 1, exercise_title)
    else:
        init_schedule.append(lesson_type)
        init_schedule.append(exercise_title)


def process_commands(init_schedule, comm):
    for one_command in comm:
        command_parts = one_command.split(':')
        actual_command = command_parts[0]
        lesson_type = command_parts[1]
        if actual_command == 'Add':
            _add(init_schedule, lesson_type)
        elif actual_command == 'Insert':
            index_to_put_the_lesson = int(command_parts[2])
            _insert(init_schedule, index_to_put_the_lesson, lesson_type)
        elif actual_command == 'Remove':
            _remove(init_schedule, lesson_type)
        elif actual_command == 'Swap':
            lesson_to_be_swapped_with_lesson_type = command_parts[2]
            _swap(init_schedule, lesson_to_be_swapped_with_lesson_type, lesson_type)
        elif actual_command == 'Exercise':
            _exercise(init_schedule, lesson_type)
    return init_schedule


initial_schedule = input().split(', ')
commands = []
while True:
    command = input()
    if command == 'course start':
        break
    commands.append(command)

final_schedule = (process_commands(initial_schedule, commands))
for count, element in enumerate(final_schedule, 1):
    print(f"{count}.{element}")
