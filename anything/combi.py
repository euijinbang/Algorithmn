def solution(arr):
    n = len(arr)

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    print(i, j, k, l)


solution([0, 1, 2, 3, 4])

# n 개 데이터에서 k 개 데이터 뽑기
# 5개 데이터에서 3개를 선택(K)
N = 4
K = 2


def combine(N, K):
    """
    K : 몇 번째 선택을 하는 것인가(깊이)
    start : 시작점
    """
    res = []

    def backtrack(start, comb):
        if len(comb) == K:
            res.append(comb.copy())
            return

        for i in range(start, N + 1):
            comb.append(i)
            backtrack(i + 1, comb)
            comb.pop()

    backtrack(1, [])
    return res

print(combine(N, K))

