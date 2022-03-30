N = 9



# cf. 열번호가 i일때 행번호의 시작위치는 i이고 끝위치는 (n//2)*2 - i 이다.


# 열과 행의 시작위치는 N // 2
# i는 행의 위치이다. 행은 j부터 N//2 + (N//2-j)+1 사이에서 1씩 증가한다.
# j는 열의 위치이다. 열은 N // 2 부터 1씩 감소한다.

# N = int(input())
list_alpha = list(map(chr, range(65, 91)))
arr = [[' '] * N for _ in range(N)]

if 1 <= N <= 100 and N % 2:
    s = 0
    for j in range(N//2, -1, -1):
        for i in range(N//2 - (N//2-j), N//2 + (N//2-j)+1):
            if s == 26:
                s = 0
            arr[i][j] = list_alpha[s]
            s += 1

    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print('')
else:
    print('INPUT ERROR')


