def sorting_cheeses(**kwargs):
    result = ''
    new_dict = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    for cheese_name, single_quantity in new_dict:
        result += f"{cheese_name}\n"
        sorted_quantity = sorted(single_quantity, reverse=True)
        result += "\n".join(str(ele) for ele in sorted_quantity) + '\n'
    return result

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)