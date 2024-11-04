deposit_sum = float(input())
deposit_time_frame = int(input())
annual_interest_rate = float(input()) / 100

sum = deposit_sum + deposit_time_frame * ((deposit_sum * annual_interest_rate) / 12)

print(sum)
