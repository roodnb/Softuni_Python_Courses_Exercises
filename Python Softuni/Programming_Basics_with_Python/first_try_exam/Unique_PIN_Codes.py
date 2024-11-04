top_first_number = int(input())
top_second_number = int(input())
top_third_number = int(input())

for x1 in range(1, top_first_number +1):
    for x2 in range(2, top_second_number +1):
        for x3 in range(1, top_third_number +1):
            if x1 % 2 == 0 and x3 % 2 == 0 and (x2 == 2 or x2 == 3 or x2 == 5 or x2 == 7):
                print (f'{x1} {x2} {x3}')


'''
drug variant : 

max_n1 = int(input())
max_n2 = int(input())
max_n3 = int(input())

for num1 in range(2, max_n1 + 1, 2):
    for num2 in range(2, max_n2 + 1):
        for num3 in range(2, max_n3 + 1, 2):
            if num2 == 2 or num2 == 3 or num2 == 5 or num2 == 7:
                print(f"{num1} {num2} {num3}")
                
za nomer 1 bachkame ot ot 2 do max nomera vkliuchitelno sys stypka 2 ( garantira ni chetno chislo
za nomer 2 bachkame ot 2 do max nomera vkliuchitelno 
za nomer 3 bachkame kato s nomer 1 
nakraq v toq if prosto kazvame ako nomer 2 ne e nqkoe ot prostite chisla i paralelno s tva che na baza nomer 1 i 3 sa prez 2 demek chetno
printira neshtata


'''