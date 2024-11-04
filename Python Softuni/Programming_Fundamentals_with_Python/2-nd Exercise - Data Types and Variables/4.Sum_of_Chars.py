number_of_characters = int(input())
total_sum = 0

for char in range(number_of_characters):
    character = input()
    total_sum += ord(character)

print(f'The sum equals: {total_sum}')