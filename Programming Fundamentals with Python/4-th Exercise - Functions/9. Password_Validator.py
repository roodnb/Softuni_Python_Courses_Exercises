def password_length(frase):
    if 6 <= len(frase) <= 10:
        return True
    else:
        return False


def password_characters(frase):
    is_valid = True
    for index in frase:
        if not (65 <= ord(index) <= 90 or 48 <= ord(index) <= 57 or 97 <= ord(index) <= 122):
            is_valid = False
            break
    return is_valid


def password_digit_requirement(frase):
    digit_count = 0
    digits = True
    for digit in frase:
        if ord(digit) in range(48, 58):
            digit_count += 1
        if digit_count < 2:
            digits = False
        else:
            digits = True
    return digits


password = input()
if password_length(password) == True \
        and password_characters(password) == True \
        and password_digit_requirement(password) == True:
    print(f'Password is valid')
if password_length(password) == False:
    print(f'Password must be between 6 and 10 characters')
if password_characters(password) == False:
    print(f'Password must consist only of letters and digits')
if not password_digit_requirement(password):
    print('Password must have at least 2 digits')