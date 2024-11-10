class MoneyNotEnoughError(Exception):
    pass


class PINCodeError(Exception):
    pass


class UnderageTransactionError(Exception):
    pass


class MoneyIsNegativeError(Exception):
    pass

pin, balance, age = list(map(int, input().split(', ')))
while True:
    current_command = input().split("#")
    command = current_command[0]

    if command == 'End':
        break

    if command == 'Send Money':
        money = int(current_command[1])
        current_pin = current_command[2]
        if float(money) > balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")

        if float(current_pin) != pin:
            raise PINCodeError("Invalid PIN code")

        if age < 18:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")

        print(f"Successfully sent {money:.2f} money to a friend")
        print(f"There is {balance - money:.2f} money left in the bank account")

    elif command == "Receive Money":
        money = int(current_command[1])
        if money < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")

        print(f"{money/2:.2f} money went straight into the bank account")
