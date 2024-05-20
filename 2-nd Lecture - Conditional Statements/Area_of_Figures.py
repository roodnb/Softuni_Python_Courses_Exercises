

figure = input()

if figure == 'square':
    a = float(input())
    area = a ** 2
    print(f"{area:.3f}") # ili s round kakto e pod-dolu ili s f-string kakto e w sluchaq
elif figure == 'rectangle':
    height = float(input())
    width = float(input())
    area = height * width
    print(round(area, 3))
elif figure == 'circle':
    from math import pi
    r = float(input())
    area = pi * r ** 2
    print(round(area, 3))
elif figure == 'triangle':
    cath = float(input())
    height = float(input())
    area = (cath * height) / 2
    print(round(area, 3))

# figure = input()
# area = 0

# if figure == 'square':
#    a = float(input())
#    area = a ** 2
#
# elif figure == 'rectangle':
#    height = float(input())
#    width = float(input())
#    area = height * width

# elif figure == 'circle':
#    from math import pi
#   r = float(input())
#    area = pi * r ** 2

# elif figure == 'triangle':
#    cath = float(input())
#    height = float(input())
#    area = (cath * height) / 2

#print(f'{area:.3}')