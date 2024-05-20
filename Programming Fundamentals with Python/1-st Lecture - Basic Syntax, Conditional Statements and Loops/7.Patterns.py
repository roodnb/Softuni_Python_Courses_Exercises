number = int(input())

for i in range(1, number + 1):
    for j in range(0, i):
        print('*', end='')
    print()

for n in range(number, 1, -1):
    for k in range(0, n-1):
        print('*', end='')
    print()


'''Първият фор цикъл казваме :
въртим i в range от 1(включително) до 3. понеже обаче прициклите когато кажем че ще въртим до 3 , то ние въртим реално само до 2
за това казваме да въртим до 3+1 , което значи че ще върти 1,2,3 ( три пъти )

Първият път когато I е реално 1-ца  вторият цикъл ще върти от 0 до 1 , което е един път и принтира една звезда.
след което първият цикъл става I = 2 , това казва на втория цикъл да върти от 0 до 2 , което е 0 и 1 демек два пъти и принтира на един
реди по една звзда


при вторият цикъл нещата седят така:
1-во n in range 3 do 1 , koeto znachi che  shte vyrti 2 pyti pri n = 3 i pri n = 2
pri vtoriqt cikyl obache , k she vyrti ot 0 do 3-1( 2 ) , poneje obache krainata granica ne se zachita to k ealn shte vyrti 0 i edno
demek dva pyti. 
'''