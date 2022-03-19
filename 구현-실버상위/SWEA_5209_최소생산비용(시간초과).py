
"""
N개의 제품, N개의 공장
제품을 1개씩 1개 공장에서 만들 때, 최소생산비용을 구하라.

순열로 풀면 시간초과날 수 있다. (N! 가지이므로 15! 은 조 단위임)
"""

import itertools
# import sys
# sys.stdin = open('input_5209.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    products = [list(map(int, input().split())) for _ in range(N)]
    factories = [x for x in range(N)]

    total_costs = []
    # 순열
    for x in itertools.permutations(factories, N):
        cost = 0
        # 공장 순서를 뽑은 하나의 순열
        factory_list = list(x)
        # 공장 하나씩 확인
        idx = 0
        for factory in factory_list:
            cost += products[idx][factory]
            idx += 1

        total_costs.append(cost)

    print("#{0} {1}".format(tc+1, min(total_costs)))
