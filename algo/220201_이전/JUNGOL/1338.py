N = 8

N = int(input())

list_alpha = list(map(chr, range(65, 91)))
arr = [[' '] * N for _ in range(N)]

r = 0
for i in range(N):          # i를 행의 위치로 잡는다.
    k = N-1
    for j in range(i, N):   # j는 행의 위치이며 i부터 n까지 증가한다.
        if r == 26:
            r = 0
        arr[j][k] = list_alpha[r]   # k는 열의 위치이며 n부터 1씩 감소한다.
        j += 1
        k -= 1
        r += 1

for i in range(N):
    for j in range(N):
        print(arr[i][j], end=' ')
    print('')