unwanted_result_number = int(input())
unwanted_result_count = 0
number_of_results = 0
result_sum = 0
number_of_tasks = 0
last_task = ''

while True:
    name_of_task = input()

    if name_of_task == 'Enough':
        average_score = result_sum / number_of_results
        print(f'Average score: {average_score:.2f}')
        print(f'Number of problems: {number_of_tasks}')
        print(f'Last problem: {last_task}')
        break
    else:
        number_of_tasks += 1

    last_task = name_of_task
    current_result = int(input())
    result_sum += current_result
    number_of_results += 1

    if current_result <= 4:
        unwanted_result_count += 1
        if unwanted_result_count == unwanted_result_number:
            print(f'You need a break, {unwanted_result_count} poor grades.')
            break


'''
drug variant s while else

unwanted_result_number = int(input())
unwanted_result_count = 0
number_of_results = 0
result_sum = 0
number_of_tasks = 0
last_task = ''

command = input()

while command != 'Enough':
    current_result = int(input())
    name_of_task = command
    last_task = name_of_task
    result_sum += current_result
    number_of_results += 1
    number_of_tasks += 1
    average_score = result_sum / number_of_results

    if current_result <= 4:
        unwanted_result_count += 1
        if unwanted_result_count == unwanted_result_number:
            print(f'You need a break, {unwanted_result_count} poor grades.')
            break

    command = input()

else:
    print(f'Average score: {average_score:.2f}')
    print(f'Number of problems: {number_of_tasks}')
    print(f'Last problem: {last_task}')


'''