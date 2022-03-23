# 열을 고정하고 행을 움직인다.

# n = 4

n = int(input())
arr = [[0] * n for _ in range(n)]
s = 1
for j in range(n):
    for i in range(n):
        arr[i][j] = s
        s += 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print('')