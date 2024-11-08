import re

class PasswordTooShortError(Exception):
    pass


class PasswordTooCommonError(Exception):
    pass


class PasswordNoSpecialCharactersError(Exception):
    pass


class PasswordContainsSpacesError(Exception):
    pass


min_pass_len = 8
special_chars = ('@', '*', '&', '%')

while True:
    password = input()
    if password == "Done":
        break

    if len(password) < min_pass_len:
        raise PasswordTooShortError("Password must contain at least 8 characters")

    if " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    if password.isalpha() or password.isdigit() or all(char in special_chars for char in password):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if not any(c in special_chars for c in password):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    print("Password is valid")