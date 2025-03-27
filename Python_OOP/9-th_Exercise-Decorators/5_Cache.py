def cache(func):

    def wrapper(n):
        if n not in wrapper.log:
            wrapper.log[n] = func(n)
        return wrapper.log[n]
    wrapper.log = {}
    return wrapper


a = 5
@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)


print(f"\n{'-----------------------------NEW TEST CODE-----------------------------'}\n")


fibonacci(4)
print(fibonacci.log)
