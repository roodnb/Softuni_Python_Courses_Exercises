import math

current_record = float(input())
distance_meters = float(input())
seconds_per_meter = float(input())

numer_of_slowness = math.floor(distance_meters / 15)
number_of_lost_seconds = (numer_of_slowness * 12.5)
# gornite 2 reda mojeshe da se napishat kato 1 : delay = floor(distance_meters / 15 ) * 12.5

ivans_record = (distance_meters * seconds_per_meter) + number_of_lost_seconds

difference_lost = abs(ivans_record - current_record)

if ivans_record < current_record:
    print(f'Yes, he succeeded! The new world record is {ivans_record:.2f} seconds.')

if ivans_record >= current_record:
    print(f'No, he failed! He was {difference_lost:.2f} seconds slower.')