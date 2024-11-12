
file = open(".\\ex_2\\numbers.txt")
# nums = [ele for ele in file.read()]
# nums = [int(ele) for ele in nums if ele != '\n']
# print(sum(nums))
# file.close()

#another solution with try except

content = file.read()
total_sum = 0

for ele in content:
    try:
        total_sum += int(ele)
    except ValueError:
        continue

print(total_sum)
file.close()