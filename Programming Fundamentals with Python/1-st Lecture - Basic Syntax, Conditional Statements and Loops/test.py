command = input()

while command != 'end':
    number = int(command)
    def odd_or_even(number):
        """Determine if a number is odd or even."""
        if number % 2 == 0:
            return 'Even'
        else:
            return 'Odd'


    print(odd_or_even(number)),
    print(odd_or_even(number))
    command = input()