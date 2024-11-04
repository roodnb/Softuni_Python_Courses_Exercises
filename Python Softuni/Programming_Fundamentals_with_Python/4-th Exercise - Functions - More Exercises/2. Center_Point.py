import math


def center_point_x(_x1, _y1, _x2, _y2):
    x = 0
    if abs(x1) <= abs(x2):
        x += x1
    else:
        x += x2
    y = 0
    if abs(y1) <= abs(y2):
        y += y1
    else:
        y += y2
    return f'({round(x)}, {round(y)})'


x1 = math.floor(float(input()))
y1 = math.floor(float(input()))
x2 = math.floor(float(input()))
y2 = math.floor(float(input()))
print(center_point_x(x1, y1, x2, y2))

# closed_x, closed_y = center_point_x(x1, y1, x2, y2)


# def center_point_y(_y1, _y2):
#     if abs(y1) <= abs(y2):
#         return y1
#     return y2

# x1 = math.floor(float(input()))
# y1 = math.floor(float(input()))
# x2 = math.floor(float(input()))
# y2 = math.floor(float(input()))
# print(center_point_x(x1, y1, x2, y2))

# print(f'({round(center_point_x(x1, x2))}, {round(center_point_y(y1, y2))})')