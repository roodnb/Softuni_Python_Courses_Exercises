def perfect_number(num):
    divisors_sum = 0
    for index in range(1,num + 1):
        if num % index == 0:
            divisors_sum += index
    if divisors_sum // 2 == num:
        return 'We have a perfect number!'
    return "It's not so perfect."


number = int(input())
print(perfect_number(number))