def even_odd_filter(**kwargs):
    new_dict = {}
    for k, v in kwargs.items():
        if k not in new_dict:
            new_dict[k] = []
            if k == 'odd':
                elements = [ele for ele in v if int(ele) % 2 != 0]
                new_dict[k] = elements
            if k == 'even':
                elements = [ele for ele in v if int(ele) % 2 == 0]
                new_dict[k] = elements

    return dict(sorted(new_dict.items(), key=lambda x: x[1], reverse=True))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
