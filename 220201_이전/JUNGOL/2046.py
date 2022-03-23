n, m = 3, 1


n, m = map(int, input().split())
arr = [[0] * n for _ in range(n)]

def style1(n, arr):
    s = 1
    for i in range(n):
        for j in range(n):
            arr[i][j] = s
        s += 1
    return arr


def style2(n, arr):
    for i in range(n):
        s = 1
        if i % 2 == 0:
            for j in range(n):
                arr[i][j] = s
                s += 1
        else:
            for j in range(n-1, -1, -1):
                arr[i][j] = s
                s += 1
    return arr

def style3(n, arr):
    for i in range(n):
        for j in range(n):
            arr[i][j] = (i+1) * (j+1)

    return arr


def result(n, arr):
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=' ')
        print('')

if m == 1:
    result(n, style1(n, arr))
elif m == 2:
    result(n, style2(n, arr))
else:
    result(n, style3(n, arr))

