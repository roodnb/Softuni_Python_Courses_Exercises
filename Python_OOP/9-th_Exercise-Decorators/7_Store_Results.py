class store_results:

    _logfile = "results.txt "

    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        result = self.function(*args)
        log_string = f"Function {self.function.__name__} was called.Result: {result}"
        with open(self._logfile, 'a') as opened_file:
            opened_file.write(log_string + '\n')
        return self.function(*args)


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
