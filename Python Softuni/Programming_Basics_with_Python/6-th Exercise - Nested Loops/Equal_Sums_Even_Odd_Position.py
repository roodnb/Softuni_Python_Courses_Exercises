x1 = int(input())
x2 = int(input())

for i in range(x1, x2 +1):
    number = str(i)
    odd_sum = 0
    even_sum = 0

    for j, digit in enumerate(number):
        if j % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    if even_sum == odd_sum:
        print(i, end=' ')


'''
drugo reshenie bez taq pederastiq enumerate :

x1 = int(input())
x2 = int(input())

for i in range(x1, x2 +1):
    number = str(i)
    odd_sum = 0
    even_sum = 0
    # dobavqme tuk oshte edno neshto koeto e promenliva(broqch na poziciqta) naprimer is_even = 1. tazi promenliva shte q polz
    vame kato vynshen broqch za preminiavane prez poziciite v chisloto koeto sega e string.
    naprimer chisloto e 1000 i pri purviq vlojen for cycle minava prez pyrvata bukva i is_even=1 ami poziciqta
    e nechetna. sled koeto predi da minem na vtorata bukva kachvame is_even s 1 = 2 chetno i tn

    for j in number
        if is_even % 2 == 0:
            even_sum += int(j)
        else:
            odd_sum += int(j)
        
        is_even += 1
    
    if even_sum == odd_sum:
        print(i, end=' ')

'''