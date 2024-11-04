def smallest(lst:list) -> int: #sys strelata kazvame che v toq list shte imame int
    most_small = min(lst)
    return most_small

first_num = int(input())
second_num = int(input())
third_num = int(input())
lowest = smallest([first_num, second_num, third_num])
print(lowest)