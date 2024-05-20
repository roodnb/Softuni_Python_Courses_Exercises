free_space_width = int(input())
free_space_length = int(input())
free_space_height = int(input())

total_space = free_space_height * free_space_width * free_space_length
boxes_placed = 0

while True:
    command = input() # също така броят на кашоните
    if command == 'Done':
        print(f'{total_space - boxes_placed} Cubic meters left.')
        break
    box = int(command)
    boxes_placed += box
    if boxes_placed > total_space:
        print(f'No more free space! You need {boxes_placed - total_space} Cubic meters more.')
        break