command = input()
house = ''
while command != 'Welcome!':
    if command == 'Voldemort':
        print('You must not speak of that name!')
        break
    commandl = len(command)
    if commandl < 5:
        house = 'Gryffindor'
    elif commandl == 5:
        house = 'Slytherin'
    elif commandl == 6:
        house = 'Ravenclaw'
    else:
        house = 'Hufflepuff'
    print(f'{command} goes to {house}.')
    command = input()

else:
    print('Welcome to Hogwarts.')