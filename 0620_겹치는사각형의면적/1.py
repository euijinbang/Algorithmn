arr = [[2, 3, 8, 7], [3, 2, 10, 6], [6, 1, 11, 4]]

x1, y1 = 0, 0
x2, y2 = 100, 100
for rec in arr:
    x1, y1 = max(x1, rec[0]), max(y1, rec[1])
    x2, y2 = min(x2, rec[2]), min(y2, rec[3])

area = (x2 - x1) * (y2 - y1)
print(x1, x2, y1, y2)
print(area)