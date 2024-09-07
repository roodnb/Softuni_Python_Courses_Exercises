number_of_electrons = int(input())
filled_shells_list = []
shell_number = 1
while number_of_electrons > 0:
    shell_max_electrons = 2 * (shell_number ** 2)
    if number_of_electrons <= shell_max_electrons:
        filled_shells_list.append(number_of_electrons)
        break
    filled_shells_list.append(shell_max_electrons)
    number_of_electrons -= shell_max_electrons
    shell_number += 1

print(filled_shells_list)