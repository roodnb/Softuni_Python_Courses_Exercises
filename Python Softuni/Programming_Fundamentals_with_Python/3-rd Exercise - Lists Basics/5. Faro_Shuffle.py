deck_of_cards = input().split()
count_of_shuffle = int(input())
middle_of_the_deck = len(deck_of_cards) // 2

for shuffle in range(count_of_shuffle):
    deck_after_shuffle = []
    left_part = deck_of_cards[:middle_of_the_deck]
    right_part = deck_of_cards[middle_of_the_deck:]
    for index in range(len(right_part)):
        deck_after_shuffle.append(left_part[index])
        deck_after_shuffle.append(right_part[index])
    deck_of_cards = deck_after_shuffle
print(deck_of_cards)
