from math import floor

def plant_garden(available_space, *plot_size, **plant_types_quantities):

    sorted_plot_size = sorted(plot_size, key=lambda x: x[0])

    sorted_plant_types_quantities = (sorted(plant_types_quantities.items(), key=lambda x: x[0]))
    count = 0

    planted = {}

    for plant in sorted_plant_types_quantities:
        type, quantity = plant
        if available_space != 0 and count != len(sorted_plant_types_quantities):
            for allowed_plant in sorted_plot_size:
                allowed, space = allowed_plant

                if type == allowed:

                    if quantity * space <= available_space:
                        available_space -= quantity * space

                    elif space <= available_space < quantity * space:
                        quantity = available_space / space
                        available_space = 0
                    else:
                        break
                    count += 1
                    if allowed not in planted:
                        planted[allowed] = 0
                    planted[allowed] += quantity

                    break

                else:
                    continue

        else:
            break

    result = []
    if available_space:
        result.append(f"All plants were planted! Available garden space: {available_space:.1f} sq meters.")
    else:
        result.append(f"Not enough space to plant all requested plants!")

    result.append("Planted plants:")

    sorted_plated = dict(sorted(planted.items()))
    for k, v in sorted_plated.items():
        result.append(f"{k}: {floor(v)}")

    return '\n'.join(result)



print('==========================================================')
print(plant_garden(50.0, ("rose", 2.5), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20))
print('==========================================================')
print(plant_garden(20.0, ("rose", 2.0), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, sunflower=5))
print('==========================================================')
print(plant_garden(2.0, ("rose", 2.5), ("tulip", 1.2), ("daisy", 0.2), rose=4, tulip=15, sunflower=3, daisy=4))
print('==========================================================')
print(plant_garden(50.0, ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, daisy=1))
print('==========================================================')