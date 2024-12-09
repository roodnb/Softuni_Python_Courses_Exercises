from ex_4.mathematical_operations import execute

string = input().split(' ')
number1 = float(string[0])
sign = string[1]
number2 = int(string[2])

print(execute(number1,sign,number2))

