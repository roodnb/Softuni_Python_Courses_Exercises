def concatenate(*args, **kwargs):
    new_str = ''
    for ele in args:
        new_str += ele

    for k, v in kwargs.items():
        if k in new_str:
            new_str = new_str.replace(k, v)

    return new_str


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
