def type_check(type):
    def decorator(function):
        def wrapper(*args, **kwargs):
            if any(not isinstance(el, type) for el in args):
                return "Bad Type"
            result = function(*args, **kwargs)
            return result
        return wrapper
    return decorator


a=5
@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))


print(f"\n{'-----------------------------NEW TEST CODE-----------------------------'}\n")


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
