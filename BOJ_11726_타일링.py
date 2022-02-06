"""
Runtime Error(Index Error)
cache = [0] * (n + 1) 이 아니라 cache [0] * 1001 을 해야 한다. why?

DP
1. memoization 을 위한 빈 리스트를 만든다.
2. 초기값을 설정한다.
3. 점화식을 기반으로 계산값을 적용한다.

초기값
f(1) = 1, f(2) = 2

점화식
f(n) = f(n-1) + f(n-2) (n >= 3)
"""
n = int(input())


def dp(n):
    cache = [0] * 1001
    cache[1] = 1
    cache[2] = 2

    for i in range(3, 1001):
        cache[i] = cache[i - 2] + cache[i - 1]
    print(cache)
    return cache[n] % 10007


print(dp(n))
