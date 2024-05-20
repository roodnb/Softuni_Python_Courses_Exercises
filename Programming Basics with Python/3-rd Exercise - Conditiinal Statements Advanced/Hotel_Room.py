month = str(input())
stay = int(input())

total_price_studio = 0
total_price_apartment = 0

price_studio_m_o = 50
price_studio_j_s = 75.20
price_studio_J_a = 76

price_apartment_m_o = 65
price_apartment_j_s = 68.70
price_apartment_J_a = 77


if stay > 14:
    if month == 'May' or month == 'October':
        total_price_studio = (price_studio_m_o * stay) * 0.7
        total_price_apartment = (price_apartment_m_o * stay) * 0.9
    elif month == 'June' or month == 'September':
        total_price_studio = (price_studio_j_s * stay) * 0.8
        total_price_apartment = (price_apartment_j_s * stay) * 0.9
    else:
        total_price_studio = price_studio_J_a * stay
        total_price_apartment = (price_apartment_J_a * stay) * 0.9

elif 7 < stay <= 14:
    if month == 'May' or month == 'October':
        total_price_studio = (price_studio_m_o * stay) * 0.95
        total_price_apartment = price_apartment_m_o * stay
    elif month == 'June' or month == 'September':
        total_price_studio = price_studio_j_s * stay
        total_price_apartment = price_apartment_j_s * stay
    elif month == 'July' or month == "August":
        total_price_studio = price_studio_J_a * stay
        total_price_apartment = price_apartment_J_a * stay

elif stay <= 7:
    if month == 'May' or month == 'October':
        total_price_studio = price_studio_m_o * stay
        total_price_apartment = price_apartment_m_o * stay
    elif month == 'June' or month == 'September':
        total_price_studio = price_studio_j_s * stay
        total_price_apartment = price_apartment_j_s * stay
    elif month == 'July' or month == "August":
        total_price_studio = price_studio_J_a * stay
        total_price_apartment = price_apartment_J_a * stay



print(f'Apartment: {total_price_apartment:.2f} lv.')
print(f'Studio: {total_price_studio:.2f} lv.')