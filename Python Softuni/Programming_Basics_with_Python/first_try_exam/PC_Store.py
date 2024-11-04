cpu_price = float(input())
gpu_price = float(input())
ram_price = float(input())
number_of_ram = int(input())
discount = float(input())


total_ram_price = number_of_ram * ram_price * 1.57
cpu_discount = cpu_price * discount
gpu_discount = gpu_price * discount

actual_cpu = (cpu_price - cpu_discount) * 1.57
actual_gpu = (gpu_price - gpu_discount) * 1.57

total_price_in_lev = (actual_gpu + actual_cpu + total_ram_price)

print(f'Money needed - {total_price_in_lev:.2f} leva.')