number = int(input())
numbers = [int(input()) for _ in range(number)]
print(f'Max number: {max(numbers)}')
print(f'Min number: {min(numbers)}')