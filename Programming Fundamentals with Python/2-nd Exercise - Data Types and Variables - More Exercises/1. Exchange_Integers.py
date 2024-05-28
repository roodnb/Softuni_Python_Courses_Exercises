a = input()
b = input()

temp_var_a = b
temp_var_b = a

a = temp_var_a
b = temp_var_b

print(f'Before:\n\
a = {temp_var_b}\n\
b = {temp_var_a}')
print(f'After:\n\
a = {temp_var_a}\n\
b = {temp_var_b}')