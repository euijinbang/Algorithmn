# 논리연산을 활용하는 문제

n = int(input())

arr = [[False] * 100 for _ in range(100)]

for _ in range(n):
    r, c = map(int, input().split())
    for i in range(r, r+10):
        for j in range(c, c+10):
            arr[i][j] = True

result = 0
for i in range(100):
    for j in range(100):
        if arr[i][j]:
            result += 1

print(result)
