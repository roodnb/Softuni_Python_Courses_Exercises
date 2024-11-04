starting_char = input()
ending_char = input()
actual_string = input()
final_result = 0

for i in range(len(actual_string)):
    if ord(starting_char) < ord(actual_string[i]) < ord(ending_char):
        final_result += ord(actual_string[i])

print(final_result)
