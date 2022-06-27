"""
1219. 길찾기
1. 순서쌍을 인접리스트로 변환
2. DFS 시작점부터 수행
3. 도착점에 도착하면 1 리턴, 한 번도 도착하지 않으면 0 리턴
"""


def dfs(v):
    global result
    if v == 99:
        result = 1
        return

    visited.add(v)

    for adj_v in adj_list[v]:
        if adj_v not in visited:
            dfs(adj_v)


for _ in range(10):
    tc, N = map(int, input().split())
    road = list(map(int, input().split()))

    adj_list = [[] for _ in range(100)]
    for i in range(N):
        st, se = road[2*i], road[2*i+1]
        adj_list[st].append(se)

    result = 0
    visited = set()
    dfs(0)

    print("#{} {}".format(tc, result))
