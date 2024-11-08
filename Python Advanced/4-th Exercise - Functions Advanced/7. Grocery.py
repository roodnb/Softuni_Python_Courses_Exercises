def grocery_store(**kwargs):
    new_dict = (sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
    return '\n'.join(f"{k}: {v}" for k, v in new_dict)
    # new_dict = dict(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
    # result = []
    # for k, v in new_dict.items():
    #     result.append(f"{k}: {v}")
    # return '\n'.join(f"{k}: {v}")


print(grocery_store(bread=5, pasta=12, eggs=12))



