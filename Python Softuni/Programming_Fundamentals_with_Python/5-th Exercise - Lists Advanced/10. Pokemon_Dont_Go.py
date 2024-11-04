distance_to_pokemon = list(map(int, input().split()))
current_sum = 0

while len(distance_to_pokemon) != 0:
    index_to_remove = int(input())
    number_to_remove = 0
    if index_to_remove > len(distance_to_pokemon) - 1:
        number_to_remove = distance_to_pokemon[-1]
        distance_to_pokemon[-1] = distance_to_pokemon[0]
    elif index_to_remove < 0:
        number_to_remove = distance_to_pokemon[0]
        distance_to_pokemon[0] = distance_to_pokemon[-1]
    else:
        number_to_remove = distance_to_pokemon.pop(index_to_remove)
    current_sum += number_to_remove
    for count, num in enumerate(distance_to_pokemon):
        if number_to_remove >= num:
            distance_to_pokemon[count] += number_to_remove
        else:
            distance_to_pokemon[count] -= number_to_remove
print(current_sum)

# The below works , but it gives 80/100 in Judge
# distance_to_pokemon = list(map(int, input().split()))
# current_sum = 0
#
# while len(distance_to_pokemon) != 0:
#     index_to_remove = int(input())
#     if index_to_remove > len(distance_to_pokemon) - 1:
#         index_to_remove = -1
#         distance_to_pokemon.append(distance_to_pokemon[0])
#     elif index_to_remove < 0:
#         index_to_remove = 0
#         distance_to_pokemon.insert(-1, distance_to_pokemon[0])
#     removed_index = distance_to_pokemon.pop(index_to_remove)
#     current_sum += removed_index
#     for count, num in enumerate(distance_to_pokemon):
#         if removed_index >= num:
#             distance_to_pokemon[count] += removed_index
#         elif removed_index < num:
#             distance_to_pokemon[count] -= removed_index
#
#
# print(current_sum)