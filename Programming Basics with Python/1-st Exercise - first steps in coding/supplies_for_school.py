box_of_pen = 5.80
box_of_marker = 7.20
cleaner = 1.20

number_of_pen_boxes = int(input())
number_of_marker_boxes = int(input())
bottle_of_cleaner = int(input())
discount = int(input()) / 100

pen_boxes_price = number_of_pen_boxes * box_of_pen
marker_boxes_price = number_of_marker_boxes * box_of_marker
cleaner_price =bottle_of_cleaner * cleaner

total_without_discount = pen_boxes_price + marker_boxes_price + cleaner_price
calculated_discount = (pen_boxes_price + marker_boxes_price + cleaner_price) * discount
total_price_to_pay_with_discount = total_without_discount - calculated_discount
print(total_price_to_pay_with_discount)




