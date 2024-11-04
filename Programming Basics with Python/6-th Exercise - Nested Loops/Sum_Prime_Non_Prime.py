command = input()
prime_sum = 0
non_prime_sum = 0

while command != 'stop':
    number = int(command)
    if number > 1:
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            prime_sum += number
        else:
            non_prime_sum += number

    elif number < 0:
        print('Number is negative.')

    command = input()
print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")
