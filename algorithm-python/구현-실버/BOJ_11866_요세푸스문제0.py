# N, K = map(int, input().split())

def josephus(n, k):
    live = [1] * (n + 1)
    live[0] = 0
    ans = []

    x = 1
    for i in range(n-1):    # n-1회 반복
        c = 1   # 지금 보는 수 x가 최근에 제거한 수로부터 몇 번째 수인지
        prev = len(ans)
        while len(ans) == prev:  # 하나의 수가 제거될 때까지 반복
            if live[x] == 1:
                if c == k:
                    live[x] = 0
                    ans.append(x)
                c += 1
            x += 1
            if x == n+1:
                x = 1

    last = live.index(1)
    ans.append(last)
    return ans


print(josephus(7, 3))


