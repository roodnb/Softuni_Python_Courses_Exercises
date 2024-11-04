import math

time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_third + time_second + time_first

minutes = total_time // 60 # celochisleno delenie naprimer 65 // 2 e ravno na 32.
seconds = total_time % 60  # towa e ravno na total_time - (minutes * 60) - тук имаме делене с остатук. в този случай остатъка е 60.
                            # naprimer 10 % 2 = 0 zashtoto nqma ostatuk. no 11 % 2 = 1 zashtoto imash ostatyk 1.
                            # v tozi sluchai naprimer 125 minuti % 60  = 5.

minutes = math.floor(minutes)

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')



