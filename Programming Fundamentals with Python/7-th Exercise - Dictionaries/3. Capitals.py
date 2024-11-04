# country = input().split(', ')
# capital = input().split(', ')
# dictionary = dict(zip(country, capital))
# for key,value in dictionary.items():
#     print(f"{key} -> {value}")


# another working example


countries = input().split(', ')
capitals = input().split(', ')
final_dictionary = {countries[index]: capitals[index] for index in range(len(capitals))}
for key, value in final_dictionary.items():
    print(f"{key} -> {value}")
