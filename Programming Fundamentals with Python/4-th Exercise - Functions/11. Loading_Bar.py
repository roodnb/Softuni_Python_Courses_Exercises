def loading_bar(provided_number):
    if provided_number == 100:
        return f'100% Complete!\n[%%%%%%%%%%]'
    loaded_percent_as_digit = provided_number // 10
    return (f"{provided_number}% [{loaded_percent_as_digit * '%'}{(10-loaded_percent_as_digit) * '.'}]\n"
            f"Still loading...")


number = int(input())
print(loading_bar(number))