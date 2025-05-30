def even_parameters(function):
    def wrapper(*args, **kwargs):
        if any(not isinstance(el, int) or el % 2 != 0 for el in args):
            return "Please use only even numbers!"
        result = function(*args, **kwargs)
        return result

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


print(f"\n{'-----------------------------NEW TEST CODE-----------------------------'}")


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))



# import unittest
#
#
# class EvenParametersTests(unittest.TestCase):
#     def test_even(self):
#         @even_parameters
#         def func(*args):
#             return sum(args)
#
#         result = func(4, 4, 4)
#         self.assertEqual(result, 12)
#
#     def test_odd(self):
#         @even_parameters
#         def func(*args):
#             return sum(args)
#
#         result = func(4, 5, 4)
#         self.assertEqual(result, "Please use only even numbers!")
#
#     def test_with_non_integer_params(self):
#         @even_parameters
#         def func(*args):
#             return sum(args)
#
#         result = func(4, "4", 4)
#         self.assertEqual(result, "Please use only even numbers!")
#
#     def test_with_no_params(self):
#         @even_parameters
#         def func():
#             return "hi"
#
#         result = func()
#         self.assertEqual(result, "hi")
#
#
# if __name__ == '__main__':
#     unittest.main()
