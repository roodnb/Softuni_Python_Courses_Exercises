def chars_are_valid(some_username):
    for char in some_username:
        if not (char.isalnum() or char == '-' or char == '_'):
            return False
    return True


def no_redundant_symbols(some_username):
    if " " in some_username:
        return False
    return True


def username_is_valid(some_usernames):
    if chars_are_valid(some_usernames) and \
            no_redundant_symbols(some_usernames):
        return True
    return False


usernames = [user for user in input().split(', ') if 3 <= len(user) <= 16]
for username in usernames:
    if username_is_valid(username):
        print(username)
