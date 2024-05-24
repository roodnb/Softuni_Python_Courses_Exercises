

'''
!!!! NOT WORKING COMPLETLEY !!!!

type_of_animal = input()
animal_list = type_of_animal.split(", ")

for animal_index in range(len(animal_list), 0, -1):
    animal = animal_list[animal_index-1]
    if animal == 'wolf':
        if animal_index < len(animal_list):
            print(f'Oi! Sheep number {animal_index-1}! You are about to be eaten by a wolf!')
        else:
            print(f'Please go away and stop eating my sheep')
'''



# # animals = input()
# # animals_list = animals.split(', ')
# # animals_list.reverse()
# # for index, animal in enumerate(animals_list):
# #     if animal == 'wolf' and index == 0:
# #         print('Please go away and stop eating my sheep')
# #     elif animal == 'wolf':
# #         print(f'Oi! Sheep number {index}! You are about to be eaten by a wolf!')
#

# name = input()
# animals = name.split(", ")
# wolf_index = animals.index('wolf') + 1
# sheep_index = len(animals) - wolf_index
# if wolf_index == len(animals):
#     print("Please go away and stop eating my sheep")
# else:
#     print(f"Oi! Sheep number {sheep_index}! You are about to be eaten by a wolf!")

