# 거꾸로 출력해야 하는 경우 배열을 새롭게 만들어주어야 한다.

# n, m = 4, 5

n, m = map(int, input().split())
arr = [[0] * m for x in range(n)]

s = 1
for i in range(n):
    if i % 2 == 0:              # 홀수행
        for j in range(m):
            arr[i][j] = s
            s += 1
    else:                       # 짝수행
        for j in range(m-1, -1, -1):
            arr[i][j] = s
            s += 1

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print('')
