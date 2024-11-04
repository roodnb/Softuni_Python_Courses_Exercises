word = input()
string_count = 0

substring_sand = "Sand"
substring_sun = 'Sun'
substring_fish = 'Fish'
substring_water = "Water"

if substring_sand.lower() in word.lower():
    string_count += word.lower().count(substring_sand.lower())

if substring_sun.lower() in word.lower():
    string_count += word.lower().count(substring_sun.lower())

if substring_fish.lower() in word.lower():
    string_count += word.lower().count(substring_fish.lower())

if substring_water.lower() in word.lower():
    string_count += word.lower().count(substring_water.lower())

print(string_count)


'''
another example

text = input()
text = text.lower()

my_list = ["sand", "water", "fish", "sun"]
counter = 0

for item in my_list:
    if item in text:
        counter += text.count(item)

print(counter)
'''