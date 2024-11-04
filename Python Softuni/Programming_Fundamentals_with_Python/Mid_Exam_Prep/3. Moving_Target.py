def shoot(_sequence, _index, _power):
    if _index in range(len(_sequence)):
        if _sequence[_index] > _power:
            _sequence[_index] -= _power
        else:
            _sequence.pop(_index)
    return _sequence


def add(_sequence, _index, _value):
    if _index in range(len(_sequence)):
        _sequence.insert(_index, _value)
    else:
        print('Invalid placement!')
    return _sequence


def strike(_sequence, _index, _radius):
    if _index - _radius not in range(len(_sequence)) \
            or _index + _radius not in range(len(_sequence)):
        print('Strike missed!')
    else:
        before_strike = _sequence[:_index - _radius]
        after_strike = _sequence[_index + _radius + 1:]
        _sequence = before_strike + after_strike
    return _sequence


sequence = list(map(int, input().split()))
command = input().split()
while command[0] != "End":
    action = command[0]
    index = int(command[1])
    if action == "Shoot":
        power = int(command[2])
        sequence = shoot(sequence, index, power)
    elif action == "Add":
        value = int(command[2])
        sequence = add(sequence, index, value)
    elif action == "Strike":
        radius = int(command[2])
        sequence = strike(sequence, index, radius)
    command = input().split()

sequence_as_string = [str(i) for i in sequence]
print('|'.join(sequence_as_string))