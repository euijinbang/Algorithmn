"""
DP
초기값
f(1) = 1
f(2) = 1
f(3) = 1
f(4) = 2
f(5) = 2

n >=6
f(n) = f(n-4) + f(n-1)
"""

N = int(input())
# 1 <= N <= 100


def dp(n):
    cache = [0] * 101
    cache[1] = 1
    cache[2] = 1
    cache[3] = 1
    cache[4] = 2
    cache[5] = 2

    for i in range(6, 101):
        cache[i] = cache[i - 1] + cache[i - 5]

    return cache[n]


for i in range(N):
    n = int(input())
    print(dp(n))
