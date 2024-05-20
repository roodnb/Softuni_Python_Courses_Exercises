number = int(input())

for i in range(1111, 9999):
    number_string = str(i)
    total_4 = 0
    for j in number_string:
        if int(j) != 0:
            if number % int(j) == 0:
                total_4 += 1

            if total_4 == 4:
                print(i, end=' ')


'''
kakvo se slcuhva tuk : 
izbirame nqkvo chislo.
sled koeto se kazva che trqbva da proverim ot vsichki chisla ot 1111 do 9999,
koito sa 4-cifreni chisla, dali nqkoq ot tehnite cifri se deli na 16.
v pyrviq cikyl kazvame , iskam na vseki cikyl da izvyrtish tezi chisla i kogato zapochne cikula , tezi chisla da se prevurnat
v string ot cifri.
sled koeto kazvame , za vsqka edna poziciq ( demek za vsqka cifra ( vuv textov format ) obyrni q pak v int i proveri dali e ravna na 0
ako ne e , to togava proveri dali ako q razdelim na 2 imam ostatuk. ako nqmame , togava zapishi v broqcha total_4 1-ca zashtoto 
realno vsichki chisla posocheni ot 1111 do 9999 sa 4 cifreni.
i nakraq kazvame , ako total 4 nqkoga stane 4 , demek vsichkite 4 cifri kato number go razdelim na tqh nqma ostatuk , 
togava mi printni tova chistlo i koeto sydyrjda tezi cifri

'''
