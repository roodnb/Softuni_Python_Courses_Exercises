def genrange(start: int, end: int):
    start_num = start
    while start_num <= end:
        yield start_num
        start_num += 1



print(list(genrange(1, 10)))