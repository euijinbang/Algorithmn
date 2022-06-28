T = int(input())

for tc in range(1, T+1):
    print("#{}".format(tc))
    N = int(input())
    cells = [list(input().split()) for _ in range(N)]

    a = []
    for i in range(N):
        for j in range(N):
            a.append(cells[N-1-j][i])  # 90도 회전

    for i in range(N):
        for j in range(N):
            a.append(cells[N-1-i][N-1-j])   # 180도 회전

    for i in range(N):
        for j in range(N):
            a.append(cells[j][N-1-i])   # 270도 회전

    for i in range(N):
        for j in range(N):
            print(''.join(a[j*N*N + i*N:j*N*N + i*N + N]), end=" ")
        print()

