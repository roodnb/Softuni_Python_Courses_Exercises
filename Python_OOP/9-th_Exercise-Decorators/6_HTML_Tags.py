def tags(something):
    def decorator(function):
        def wrapper(*args, **kwargs):
            result = function(*args)
            return f"<{something}>{result}</{something}>"

        return wrapper
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))


print(f"\n{'-----------------------------NEW TEST CODE-----------------------------'}\n")


@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))
