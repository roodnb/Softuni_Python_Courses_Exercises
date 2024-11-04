number_of_snowballs = int(input())

bestsnowball = 0
weight_count = 0
time_count = 0
quality_count = 0

for snowball in range(number_of_snowballs):
    weight_of_the_snowball = int(input())
    time_to_target = int(input())
    quality = int(input())
    snowball_value = (weight_of_the_snowball / time_to_target) ** quality
    if snowball_value > bestsnowball:
        bestsnowball = snowball_value
        weight_count = weight_of_the_snowball
        time_count = time_to_target
        quality_count = quality

print(f'{weight_count} : {time_count} = {int(bestsnowball)} ({quality_count})')

