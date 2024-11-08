string = input()
uniques = {index for index in string}
for ch in sorted(uniques):
    print(f"{ch}: {string.count(ch)} time/s")







# solution with dictionary
#
# string = input()
# uniques = {}
# for i in string:
#     if i not in uniques:
#         uniques[i] = 0
#     uniques[i] += 1
# for k, v in sorted(uniques.items()):
#     print(f' {k}: {v} time/s')