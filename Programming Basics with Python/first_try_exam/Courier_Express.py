weight = float(input())
delivery_type = input()
distance = int(input())



if delivery_type == 'standard':
    if 0 < weight < 1:
        overall = distance * 0.03
    elif 1 <= weight < 10:
        overall = distance * 0.05
    elif 10 <= weight < 40:
        overall = distance * 0.10
    elif 40 <= weight < 90:
        overall = distance * 0.15
    else:
        overall = distance * 0.20

elif delivery_type == 'express':
    if 0 < weight < 1:
        price = distance * 0.03
        express_commission_per_kg = 0.03 * 0.8
        total_express_commission_per_kg = weight * express_commission_per_kg
        total_commission = distance * total_express_commission_per_kg
        overall = price + total_commission
    elif 1 <= weight < 10:
        price = distance * 0.05
        express_commission_per_kg = 0.05 * 0.4
        total_express_commission_per_kg = weight * express_commission_per_kg
        total_commission = distance * total_express_commission_per_kg
        overall = price + total_commission
    elif 10 <= weight < 40:
        price = distance * 0.10
        express_commission_per_kg = 0.10 * 0.05
        total_express_commission_per_kg = weight * express_commission_per_kg
        total_commission = distance * total_express_commission_per_kg
        overall = price + total_commission
    elif 40 <= weight < 90:
        price = distance * 0.15
        express_commission_per_kg = 0.15 * 0.02
        total_express_commission_per_kg = weight * express_commission_per_kg
        total_commission = distance * total_express_commission_per_kg
        overall = price + total_commission
    else:
        price = distance * 0.2
        express_commission_per_kg = 0.2 * 0.01
        total_express_commission_per_kg = weight * express_commission_per_kg
        total_commission = distance * total_express_commission_per_kg
        overall = price + total_commission



print(f'The delivery of your shipment with weight of {weight:.3f} kg. would cost {overall:.2f} lv.')