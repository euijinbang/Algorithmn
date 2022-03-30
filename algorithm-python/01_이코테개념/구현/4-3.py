pos = 'a1'
print(ord('a'))
x, y = int(pos[1])-1, int(ord(pos[0]) - 97)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

count = 0
for i in range(4):
    x += 2 * dx[i]
    y += 2 * dy[i]

    if i == 0 or i == 1:
        for j in range(2, 4):
            x += dx[j]
            y += dy[j]

            if x < 0 or y < 0 or x >= 8 or y >= 8:
                pass
            else:
                count += 1

    if i == 2 or i == 3:
        for j in range(0, 2):
            x += dx[j]
            y += dy[j]

            if x < 0 or y < 0 or x >= 8 or y >= 8:
                pass
            else:
                count += 1

print(count)