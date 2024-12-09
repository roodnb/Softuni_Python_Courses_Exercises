def create_seq(count):
    seq = []
    for num in range(count):
        if len(seq) >= 2:
            seq.append(seq[-1] + seq[-2])
        else:
            seq.append(num)
    return seq


def locate_seq(num, seq):
    for index, value in enumerate(seq):
        if value == num:
            return f"The number - {num} is at index {index}"
    return f"The number - {num} is not in the sequence"


#another option
# def locate_seq(num, seq):
#     try:
#         seq.index(num)
#         return f"The number - {num} is at index {seq.index(num)}"
#     except ValueError:
#         return f"The number - {num} is not in the sequence"