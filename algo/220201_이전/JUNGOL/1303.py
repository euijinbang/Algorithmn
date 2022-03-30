n, m = 4, 5


# n, m = map(int, input().split())

s = 1
for i in range(n):
    for j in range(m):
        print(s, end=' ')
        s += 1
    print('')