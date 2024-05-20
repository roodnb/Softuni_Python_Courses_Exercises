number_of_groups = int(input())


Musala = 0
Monblanc = 0
Kilimanjaro = 0
K2 = 0
Everest = 0

peak_percent = 0
total_number_of_people = 0


for group in range(number_of_groups):
    number_of_ppl = int(input())
    total_number_of_people += number_of_ppl
    if 0 < number_of_ppl <= 5:
        Musala += number_of_ppl
    elif 6 <= number_of_ppl <= 12:
        Monblanc += number_of_ppl
    elif 13 <= number_of_ppl <= 25:
        Kilimanjaro += number_of_ppl
    elif 26 <= number_of_ppl <= 40:
        K2 += number_of_ppl
    else:
        Everest += number_of_ppl


print(f'{Musala/total_number_of_people*100:.2f}%')
print(f'{Monblanc/total_number_of_people*100:.2f}%')
print(f'{Kilimanjaro/total_number_of_people*100:.2f}%')
print(f'{K2/total_number_of_people*100:.2f}%')
print(f'{Everest/total_number_of_people*100:.2f}%')

