import re

barcode_count = int(input())
valid_barcode_pattern = r'@([#]+)([A-Z]([a-zA-Z0-9]{4,})+[A-Z])@([#]+)'
barcode_list = []
for code in range(barcode_count):
    barcode = input()
    matches = re.findall(valid_barcode_pattern, barcode)
    product_group_pattern = r'\d+'
    if matches:
        for match in matches:
            valid_barcode = (match[1])
            digit_matches = re.findall(product_group_pattern, valid_barcode)
            if len(digit_matches) > 0:
                print(f"Product group: {''.join(digit_matches)}")
            else:
                print('Product group: 00')
    else:
        print('Invalid barcode')

