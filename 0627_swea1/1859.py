"""
1859. 백만장자 프로젝트
<< Two Pointer >>

가격 1 1 3 1 2  / 이익 5
sol1.
- 1. max 갱신 + 차례로 돌면서 내 뒤에 나보다 큰 값이 나오면 사도된다 체크
- 2. 다시 돌면서 cost, cnt 갱신
- 3. 최종 이익 계산 (profit = max * cnt - cost)

sol2.
- 1. 맨 뒤 value 를 최대로 설정
- 2. 거꾸로 앞으로 가면서 max보다 작으면 차익 +
- 3. max 보다 크면 max 갱신
- 4. 끝까지 반복
"""

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cost = list(map(int, input().split()))  # 10, 7, 6
    ans = 0

    # sol2. 뒤부터 체크, max 갱신하며 이득 추가
    max_cost = cost[-1]
    for i in range(N-1, -1, -1):
        if cost[i] < max_cost:
            ans += max_cost - cost[i]
        else:
            max_cost = cost[i]

    # sol1. 사는날과 파는 날 표시
    # is_sell = [False] * N
    # for i in range(N-1):
    #     for j in range(i+1, N):
    #         if cost[i] < cost[j]:
    #             is_sell[i] = True
    #             break
    #
    # buy_cost, buy_cnt = 0, 0
    # for i in range(N):
    #     if is_sell[i]:
    #         buy_cost += cost[i]
    #         buy_cnt += 1
    #     else:
    #         ans += (cost[i] * buy_cnt) * buy_cost
    #         buy_cost, buy_cnt = 0, 0

    # sol0. 매번마다 내 뒤의 인덱스부터 max 구해서
    # 현재값이 더 작으면 사서판다. => 시간초과

    # for i in range(N-1): # 마지막 날은 사도 그만 안사도 그만
    #     max_cost = cost[i]
    #     for j in range(i+1, N):
    #         if max_cost < cost[j]:
    #             max_cost = cost[j]
    #
    #         if max_cost > cost[i]:
    #             ans += max_cost - cost[i]

    print("#{} {}".format(tc, ans))
