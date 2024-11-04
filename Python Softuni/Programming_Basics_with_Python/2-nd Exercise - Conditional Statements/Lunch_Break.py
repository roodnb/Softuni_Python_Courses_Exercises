import math

tv_show_name = str(input())
time_per_episode = int(input())
brake_length = int(input())

time_for_lunch = brake_length / 8
relax_time = brake_length / 4

time_left_to_watch = (brake_length - time_for_lunch - relax_time)

if_enough = math.ceil(time_left_to_watch - time_per_episode)
if_not = math.ceil(time_per_episode - time_left_to_watch)


if time_per_episode <= time_left_to_watch:
    print(f'You have enough time to watch {tv_show_name} and left with {if_enough} minutes free time.')

if time_per_episode > time_left_to_watch:
    print(f"You don't have enough time to watch {tv_show_name}, you need {if_not} more minutes.")