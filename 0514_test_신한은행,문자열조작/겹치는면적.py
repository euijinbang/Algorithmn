b = [[0]*100 for _ in range(100)]
# info = [[2, 3, 8, 7], [3, 2, 10, 6], [6, 1, 11, 4]]
# info = [[0, 0, 2, 2], [2, 2, 4, 4]]

for i in info:
    x1, y1, x2, y2 = i[0], i[1], i[2], i[3]
    for m in range(x1, x2):
        for n in range(y1, y2):
            b[m][n] += 1

max_result = 0
for row in b:
    max_result = max(max(row), max_result)

print(max_result)
ans = 0
for i in range(100):
    for j in range(100):
        if b[i][j] == 3:
            ans += 1

print(ans)
