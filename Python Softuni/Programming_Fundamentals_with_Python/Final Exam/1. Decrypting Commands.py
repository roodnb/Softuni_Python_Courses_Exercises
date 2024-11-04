text = input()
while True:
    command = input().split(' ')

    if command[0] == 'Finish':
        break

    action = command[0]

    if action == 'Replace':
        current_char = command[1]
        new_char = command[2]
        text = text.replace(current_char, new_char)
        print(text)

    elif action == 'Cut':
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(text) and 0 <= end_index < len(text):
            text = text[:start_index] + text[end_index + 1:]
            print(text)
        else:
            print(f"Invalid indices!")

    elif action == 'Make':
        upper_lower = command[1]
        if upper_lower == "Upper":
            text = text.upper()
        elif upper_lower == 'Lower':
            text = text.lower()
        print(text)

    elif action == 'Check':
        string = command[1]
        if string in text:
            print(f'Message contains {string}')
        else:
            print(f"Message doesn't contain {string}")

    elif action == 'Sum':
        start_idk = int(command[1])
        end_idk = int(command[2])
        current_sum = 0
        if start_idk < 0 or start_idk >= len(text) or end_idk < 0 or end_idk >= len(text):
            print(f"Invalid indices!")
        else:
            substring = text[start_idk:end_idk + 1]
            for i in substring:
                current_sum += ord(i)
            print(current_sum)

