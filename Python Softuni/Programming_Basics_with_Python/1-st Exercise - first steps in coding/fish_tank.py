length = int(input())
width =  int(input())
height = int(input())
percentage_of_non_watter = float(input()) / 100

total_load = length * width * height
no_watter = percentage_of_non_watter * total_load

actual_watter = (total_load - no_watter) / 1000

print(actual_watter)