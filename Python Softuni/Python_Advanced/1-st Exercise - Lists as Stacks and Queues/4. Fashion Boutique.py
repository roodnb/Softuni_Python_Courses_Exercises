box_of_clothes = list(map(int, input().split()))
one_rack_capacity = int(input())

value_sum = 0
rack_count = 1

while box_of_clothes:
    if one_rack_capacity == value_sum or one_rack_capacity < value_sum + box_of_clothes[-1]:
        rack_count += 1
        value_sum = 0
    value_sum += box_of_clothes.pop()

print(rack_count)