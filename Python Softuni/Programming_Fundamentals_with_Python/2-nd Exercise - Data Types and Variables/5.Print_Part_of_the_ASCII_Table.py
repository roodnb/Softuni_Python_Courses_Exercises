first_number = int(input())
second_number = int(input())
character = ''
for i in range(first_number, second_number + 1):
    character = chr(i)
    print(character, end=' ')

'''
another example

for i in range(first_number, second_number + 1):
    print(chr(i), end' ')  
    
In this particular case , however we do not remove the last space after the string.  
In order to do that we can one if in the cycle and in this if we say 
if character == second_number
    print(chr(character))
else
    print(character, end=' ')
    
antoher example is for us to create a new string and put each value in the new string and use the strip
function to remove the spaces.
'''