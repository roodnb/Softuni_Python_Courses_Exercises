file = input().split("\\")
last_index = file[-1].split('.')
print(f'File name: {last_index[0]}')
print(f'File extension: {last_index[1]}')