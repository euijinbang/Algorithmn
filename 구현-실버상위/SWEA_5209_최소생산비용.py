"""
N개의 제품, N개의 공장
제품을 1개씩 1개 공장에서 만들 때, 최소생산비용을 구하라.

가지자르기, DFS(재귀), 방문체크...
"""

import sys
sys.stdin = open('input_5209.txt', 'r')

T = int(input())


def factory(idx, s):  # 제품번호, 중간 계산결과
    global ans
    if idx == N:
        if s < ans:
            ans = s
        return ans
    elif s >= ans:
        return
    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                factory(idx+1, s + cost[idx][i])   # 기존비용 + 이번 제품비용(idx 제품 i공장 생산)
                visited[i] = 0                     # 초기화


for tc in range(T):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]

    ans = 987654321
    visited = [0] * N
    factory(0, 0)

    print("#{0} {1}".format(tc+1, ans))
