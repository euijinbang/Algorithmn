"""
DP Dynamic Programming : Top-down with memoization

f(x) = f(x-1) + 1
f(x) = f(x//2) + 1
f(x) = f(x//3) + 1

초기값 f(1) = 0
"""

N = int(input())


def dp(N):
    min_cnt = [0] * (N + 1)     # 연산 횟수
    route = [[1]] * (N + 1)       # 경로

    min_cnt[1] = 0      # 초기값 1의 연산 횟수는 0

    for i in range(2, N+1):

        min_cnt[i] = min_cnt[i - 1] + 1
        route[i] = route[i-1] + [i]

        # 3가지 방법 중 연산 횟수가 더 적은 경우로 갱신됨, 루트도 갱신됨
        if i % 2 == 0 and min_cnt[i // 2] + 1 < min_cnt[i]:
            min_cnt[i] = min_cnt[i // 2] + 1
            route[i] = route[i//2] + [i]

        if i % 3 == 0 and min_cnt[i // 3] + 1 < min_cnt[i]:
            min_cnt[i] = min_cnt[i // 3] + 1
            route[i] = route[i//3] + [i]

    # print(route)
    # print(min_cnt)
    return min_cnt, route


min_cnt, route = dp(N)
print(min_cnt[N])

r = route[N]
print(*r[::-1])


