def create_upper_part(num):
    for row in range(1, num + 1):
        print(" "*(num-row) + "* "*row)


def create_lower_part(num):
    for row in range(num - 1, 0, -1):
        print(" "*(num-row) + "* "*row)


def create_rhombus(num):
    create_upper_part(num)
    create_lower_part(num)


n = int(input())
create_rhombus(n)


# Another resolution:

# def print_row(spaces, stars):
#     print(' '*spaces + '* '*stars)
#
#
# def print_upper(n):
#     for row in range(1, n + 1):
#         spaces = n-row
#         print_row(spaces,row)
#
#
# def print_lower(n):
#     for row in range(1, n):
#         stars = n-row
#         print_row(row, stars)
#
#
# def print_rhombus(n):
#     print_upper(n)
#     print_lower(n)
#
#
# n = int(input())
# print_rhombus(n)
