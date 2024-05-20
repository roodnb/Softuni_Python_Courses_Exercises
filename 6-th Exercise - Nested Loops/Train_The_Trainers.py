jury = int(input())

command = input()
command_counter = 0
current_command_total_result = 0
total_average = 0

while command != 'Finish':
    for i in range(jury):
        jury_results = float(input())
        current_command_total_result += jury_results

    average_current_command_result = current_command_total_result / jury
    total_average += average_current_command_result
    print(f'{command} - {average_current_command_result:.2f}.')
    current_command_total_result = 0

    command_counter += 1
    command = input()

else:
    print(f"Student's final assessment is {total_average / command_counter:.2f}.")



'''
jury = int(input())
total_number_of_presentation = 0
total_score_from_presentation = 0

while True:
    command = input()
    if command == 'Finish':
        print(f"Student's final assesment is {total_score_from_presentation/total_number_of_presentation:.2f}")
        break
    else:
        presentation = ''
        presentation = command
        sum_score = 0 
        
        for i in range(jury):
            score = float(input())
            sum_score += score
            total_score_from_presentation += score
            total_number_of_presentation += 1
            
        print(f"{presentation} - {sum_score/jury:.2f}.")


'''