text = input()

try:
    times = int(input())
    print(text*times)
except ValueError:
    print("Variable times must be an integer")


# или друг вариянт:

try:
    times = int(input())
except ValueError:
    print("Variable times must be an integer")
else:
    print(text * times)