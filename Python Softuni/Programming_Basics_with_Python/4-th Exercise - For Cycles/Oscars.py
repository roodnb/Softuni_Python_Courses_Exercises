name = str(input())
academy_points = float(input())
jury = int(input())

actor_points = 0
points_given_by_jury = 0

for points in range(1, jury +1):
    jury_name = str(input())
    jury_points = float(input())
    points_given_by_jury = (len(jury_name) * jury_points)/2
    actor_points += points_given_by_jury
    if actor_points + academy_points >= 1250.5:
        break

if actor_points >=1250.5 - academy_points:
    print(f'Congratulations, {name} got a nominee for leading role with {actor_points + academy_points:.1f}!')
else:
    print(f'Sorry, {name} you need {1250.5 - (actor_points + academy_points):.1f} more!')



'''
друг вариянт за решението е :

name = str(input())
academy_points = float(input())
jury = int(input())

total_points = academy_points

for i in range(jury):
    jury_name = str(input())
    jury_points = float(input())
    if total_points <= 1250.5
        total_points += (len(jury_name) * jury_points)/2
    else:
        break

if total_ponts >= 1250.5
    print nam si kvo si
else:
    print edi kvo si
    

'''