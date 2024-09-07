notes = [0] * 10

while True:
    command = input()
    if command == 'End':
        break
    current_command = command.split('-')
    priority = int(current_command[0]) - 1 # tova go pravin zashtoto spisykat ima 10 pozicii ot 1 do 10,
    # no realno 1-cata e index 0 a pyrviyat input e 3. troikata realno se qvqva na index 2
    note = current_command[1]
    notes.pop(priority)
    notes.insert(priority, note)

result = [element for element in notes if element != 0]
print(result)