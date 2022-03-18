N = 5
plans = ['R', 'R', 'R', 'U', 'D', 'D']

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 1, 1
position = 0
# 우-하-좌-상
for plan in plans:
    if plan == 'R':
        position = 0
    if plan == 'D':
        position = 1
    if plan == 'L':
        position = 2
    if plan == 'U':
        position = 3

    if x + dx[position] < 1 or x + dx[position] > N or y + dy[position] < 1 or y + dy[position] > N:
        continue

    x += dx[position]
    y += dy[position]

print(x, y)
