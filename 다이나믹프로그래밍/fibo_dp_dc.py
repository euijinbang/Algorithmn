"""
DP Dynamic Programming : Top-down with memoization
DC Divide and Conquer : Bottom-up with recursive
"""


def fibo_dc(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fibo_dc(n-1) + fibo_dc(n-2)


print(fibo_dc(5))


def fibo_dp(n):
    cache = [0 for x in range(n + 1)]
    cache[0] = 0
    cache[1] = 1

    for i in range(2, n + 1):
        cache[i] = cache[i - 1] + cache[i - 2]

    return cache[n]


print(fibo_dp(5))
