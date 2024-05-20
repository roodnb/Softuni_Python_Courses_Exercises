command = input()

total_tickets = 0
total_student = 0
total_standard = 0
total_kid = 0
while command != 'Finish':
    free_seats = int(input())
    student_tickets = 0
    standard_tickets = 0
    kids_tickets = 0
    tickets_sold = 0
    for j in range(free_seats):
        type_of_seat = input()
        if type_of_seat == 'student':
            student_tickets += 1
            total_student += 1
        elif type_of_seat == 'standard':
            standard_tickets += 1
            total_standard += 1
        elif type_of_seat == 'kid':
            kids_tickets += 1
            total_kid += 1

        if tickets_sold == free_seats or type_of_seat == 'End':
            print(f'{command} - {tickets_sold / free_seats * 100:.2f}% full.')
            break

        tickets_sold += 1
    total_tickets += tickets_sold
    command = input()

else:
    print(f'Total tickets: {total_tickets}')
    print(f'{total_student / total_tickets * 100:.2f}% student tickets.')
    print(f'{total_standard / total_tickets * 100:.2f}% standard tickets.')
    print(f'{total_kid / total_tickets * 100:.2f}% kids tickets.')