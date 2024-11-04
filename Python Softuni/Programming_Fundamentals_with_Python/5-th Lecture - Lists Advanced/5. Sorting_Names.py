names = input().split(', ')
sorted_names = sorted(names, key=lambda name: (-len(name), name))
# poneje key, moje da prieme samo edna stoinost a nie iskame da sortirame po 2 nachina za tova
# izpolzvame lambda. v tozi sluchai nie kazvame funkciata lambda da sortira 1-vo po duljina kato zapochva ot nai dulgoto
# i posle po ime , koeto e po azbuchen red.
print(sorted_names)