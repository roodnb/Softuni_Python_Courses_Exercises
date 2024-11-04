def fill_the_box(*args):
    size = args[0] * args[1] * args[2]
    cubes = 0
    for index in range(3, len(args)):
        if args[index] == 'Finish':
            break
        else:
            cubes += args[index]

    if size > cubes:
        return f"There is free space in the box. You could put {size - cubes} more cubes."
    else:
        return f"No more free space! You have {cubes - size} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))