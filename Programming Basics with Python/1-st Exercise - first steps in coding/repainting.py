cover_price = 1.50
paint_price = 14.50
thinner_price = 5.00
bags_price = 0.40


covers = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

required_covers_price = (covers + 2) * cover_price
required_paint = (paint + (paint * 0.1)) * paint_price
required_thinner_price = thinner * thinner_price
workers_price_per_hour = (required_covers_price + required_paint + required_thinner_price + bags_price) * 0.30
required_hours = hours * workers_price_per_hour


sum = required_covers_price + required_paint + required_thinner_price + required_hours + bags_price

print(sum)