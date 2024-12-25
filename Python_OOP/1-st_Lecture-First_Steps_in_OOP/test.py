def print_row(size, star_count):
    for row in range(size - star_count):
        print(".", end="")
    for row in range(1, star_count):
        print("*", end=".")
    print('*')

size = int(input())
for star_count in range(1, size):
    print_row(size, star_count)
for star_count in range(size, 0, -1):
    print_row(size, star_count)





# sys space-ove zashtoto vtoriq for cikul vyrti 1 pyt poveche ot gorniq sluchai.


def print_row(size, star_count):
    for row in range(size - star_count):
        print(".", end="")
    for row in range(1, star_count + 1):
        print("*", end=".")
    print()

size = int(input())
for star_count in range(1, size):
    print_row(size, star_count)
for star_count in range(size, 0, -1):
    print_row(size, star_count)