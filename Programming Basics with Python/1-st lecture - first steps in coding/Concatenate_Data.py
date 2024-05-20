first_name = input()
last_name = input()
age = str(int(input()))
town = input()


print('You are', first_name, last_name, age + '-years old person from', town)


#if age = int(input) the above will not work due to the fact that you can not glue int and str
#age = int(input) will expect a number. age =str(int(input))) - the number will inputed will be a string.
#so if age = int(input) the below is the way to work with F-string WHICH IS THE SUGGESTED BETTER WAY
# print (f'You are {first_name} {last_name}, a {age}-years old person from {town}.')

