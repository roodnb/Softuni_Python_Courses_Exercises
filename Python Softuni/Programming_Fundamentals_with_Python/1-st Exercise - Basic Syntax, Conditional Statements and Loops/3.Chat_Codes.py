number_of_messages = int(input())

for n in range(number_of_messages):
    number = int(input())
    command = ''
    if number == 88:
        command = 'Hello'
    elif number == 86:
        command = 'How are you?'
    elif number == 87 or number < 86:
        command = 'GREAT!'
    else:
        command = 'Bye.'
    print(f'{command}')