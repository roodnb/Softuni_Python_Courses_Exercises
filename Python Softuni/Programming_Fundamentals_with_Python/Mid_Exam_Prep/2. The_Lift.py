waiting_people = int(input())
lift_state = list(map(int, input().split()))


for wagon in range(len(lift_state)):
    if waiting_people > 0:
        current_num_of_people = 4 - int(lift_state[wagon])
        if waiting_people < current_num_of_people:
            lift_state[wagon] += waiting_people
            waiting_people -= waiting_people
        else:
            waiting_people -= current_num_of_people
            lift_state[wagon] += current_num_of_people


if waiting_people > 0:
    print(f"There isn't enough space! {waiting_people} people in a queue!")
elif sum(lift_state) != len(lift_state) * 4:
    print(f'The lift has empty spots!')

print(' '.join(str(num) for num in lift_state))
