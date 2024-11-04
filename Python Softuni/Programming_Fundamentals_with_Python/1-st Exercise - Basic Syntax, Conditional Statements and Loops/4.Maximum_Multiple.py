# divisor = int(input())
# boundary = int(input())
# maxN = 0
# for N in range(1, boundary + 1):
#     if N % divisor == 0:
#         maxN = N
# print(maxN)

# another resolution is to start from high to low.

divisor = int(input())
boundary = int(input())
for n in range(boundary, 0, -1):
    if n % divisor == 0:
        print(n)
        break

# another solution:
#largest_number = boundry - (boundry % devisor)
#print(largest_number)


# another solution:
#largest_number = (boundary//divisor)*divisor
#print(largest_number)