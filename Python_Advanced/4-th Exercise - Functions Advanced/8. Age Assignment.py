def age_assignment(*args, **kwargs):
    new_dict = {}
    # result = []
    for name in args:
        new_dict[name] = kwargs[name[0]]
        # for k, v in kwargs.items():
        #     if name.startswith(k):
        #         new_dict[name] = v
    new_dict = sorted(new_dict.items(), key=lambda x: x[0])
    # for ele in new_dict:
    #     result.append(f"{ele[0]} is {ele[1]} years old.")

    return '\n'.join(f"{name} is {age} years old." for name, age in new_dict)


print(age_assignment("Peter", "George", G=26, P=19))