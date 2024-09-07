def add_phone(_phones_list, _phone_to_add):
    if _phone_to_add not in _phones_list:
        _phones_list.append(_phone_to_add)
    return _phones_list


def remove_phone(_phones_list, _phone_to_be_removed):
    if _phone_to_be_removed in _phones_list:
        _phones_list.remove(_phone_to_be_removed)
    return _phones_list


def bonus_phone(_phones_list, _old_phone, _new_phone):
    if _old_phone in _phones_list:
        _old_phone_idx = _phones_list.index(_old_phone)
        _phones_list.insert(_old_phone_idx + 1, _new_phone)
    return _phones_list


def last_phone(_phones_list, _current_last_phone):
    if _current_last_phone in _phones_list:
        _current_last_phone_idx = _phones_list.index(_current_last_phone)
        _phones_list.append(_phones_list.pop(_current_last_phone_idx))
    return _phones_list


phones_list = input().split(', ')
command = input().split(' - ')
while command[0] != "End":
    action = command[0]
    if action == "Add":
        phone_to_add = command[1]
        phones_list = add_phone(phones_list, phone_to_add)
    elif action == "Remove":
        phone_to_be_removed = command[1]
        phones_list = remove_phone(phones_list, phone_to_be_removed)
    elif action == "Bonus phone":
        current_bonus_phones = command[1].split(':')
        old_phone = current_bonus_phones[0]
        new_phone = current_bonus_phones[1]
        phones_list = bonus_phone(phones_list, old_phone, new_phone)
    elif action == 'Last':
        current_last_phone = command[1]
        phones_list = last_phone(phones_list, current_last_phone)
    command = input().split(' - ')
print(', '.join(phones_list))