def even_odd(*lst):
    result = []
    if lst[-1] == "even":
        elements = [ele for ele in lst[0: -1] if int(ele) % 2 == 0]
        result.extend(elements)
    elif lst[-1] == "odd":
        elements = [ele for ele in lst[0: -1] if int(ele) % 2 != 0]
        result.extend(elements)

    return result


print(even_odd(6, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))