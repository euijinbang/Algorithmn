N = int(input())
su = list(map(int, input().split()))
# N = 6
# su = [10, 20, 10, 30, 20, 50]

d = [0] * (N + 1)

for i in range(N):
    for j in range(i):
        if su[i] > su[j]:
            d[i] = max(d[i], d[j] + 1)

print(max(d)+1)


