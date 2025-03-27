# def hello_function():
#     def say_hi():
#         return "Hi"
#     return say_hi
#
#
# hello = hello_function()
# print(hello())
#
#
#
#
# from functools import wraps
#
# def uppercase(function):
#     @wraps(function)
#     def wrapper():
#         result = function()
#         uppercase_result = result.upper()
#         return uppercase_result
#     return wrapper










class func_logger:

    _logfile = 'out.log'

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        log_string = self.func.__name__ + " was called"
        with open(self._logfile, 'a') as opened_file:
            opened_file.write(log_string + '\n')
        return self.func(*args)


@func_logger
def say_hi(name):
    print(f"Hi, {name}")


@func_logger
def say_bye(name):
    print(f"Bye, {name}")


say_hi("Peter")
say_bye("Peter")