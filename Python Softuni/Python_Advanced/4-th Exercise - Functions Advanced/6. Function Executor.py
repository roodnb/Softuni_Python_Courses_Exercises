
def func_executor(*args):
    result = []
    for ele in args:
        function = ele[0]
        data = ele[1]
        result.append(f"{function.__name__} - {function(*data)}")

    return '\n'.join(result)


def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result

def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result

print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))

