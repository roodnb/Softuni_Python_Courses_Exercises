num_of_pieces = int(input())

pianist_dict = {}
for item in range(num_of_pieces):
    piece, composer, key = input().split('|')
    pianist_dict[piece] = {'composer': composer, 'key': key}

command = input().split('|')

while command[0] != 'Stop':
    current_command = command[0]
    if current_command == 'Add':
        current_piece = command[1]
        current_composer = command[2]
        current_key = command[3]
        if current_piece not in pianist_dict:
            pianist_dict[current_piece] = {'composer': current_composer, 'key': current_key}
            print(f'{current_piece} by {current_composer} in {current_key} added to the collection!')
        else:
            print(f'{current_piece} is already in the collection!')
    elif current_command == 'Remove':
        current_piece = command[1]
        if current_piece in pianist_dict:
            del pianist_dict[current_piece]
            print(f'Successfully removed {current_piece}!')
        else:
            print(f'Invalid operation! {current_piece} does not exist in the collection.')
    elif current_command == 'ChangeKey':
        current_piece = command[1]
        current_key = command[2]
        if current_piece in pianist_dict:
            pianist_dict[current_piece]['key'] = current_key
            print(f'Changed the key of {current_piece} to {current_key}!')
        else:
            print(f'Invalid operation! {current_piece} does not exist in the collection.')

    command = input().split('|')

for piece, info in pianist_dict.items():
    print(f"{piece} -> Composer: {info['composer']}, Key: {info['key']}")