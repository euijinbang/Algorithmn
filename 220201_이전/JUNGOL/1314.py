# n = 9

n = int(input())

list_alpha = list(map(chr, range(65, 91)))
arr = [[0] * n for _ in range(n)]

s = 0
for j in range(n):
    if j % 2 ==  0:  # 짝수열
        for i in range(n):
            if s == 26:
                s = 0
            arr[i][j] = list_alpha[s]
            s += 1
    else:            # 홀수열
        for i in range(n-1, -1, -1):
            if s == 26:
                s = 0
            arr[i][j] = list_alpha[s]
            s += 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print('')
