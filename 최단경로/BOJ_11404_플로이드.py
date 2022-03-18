# INF 설정으로 인한 실패 => INF = 100000 * 100(최대 도시의 개수) 로 변경
# 메모리 초과 문제 => INF = 100000 * 100(최대 도시의 개수)

# 플로이드_와샬
import sys

INF = 10000000

n = int(sys.stdin.readline())  # 노드 수
m = int(sys.stdin.readline())  # 간선 수

# 현재까지 계산된 최소비용 초기화
d = []
for x in range(n):
    d.append([INF] * n)

for _ in range(m):
    st_node, end_node, val = map(int, sys.stdin.readline().split())
    # 경로 1개이상인 경우(존재하는 경우) 더 비용적은 경로로 선택
    if val < d[st_node-1][end_node-1]:
        d[st_node - 1][end_node - 1] = val
    else:
        pass
    d[st_node-1][st_node-1] = 0

# print(d)
# k = 거쳐가는 노드, i = 출발 노드, j = 도착 노드
for k in range(n):
    for i in range(n):
        for j in range(n):
            # 출발-도착 직선거리보다 특정 노드를 거쳐가는 비용을 비교해서 더 적은 비용으로 초기화한다.
            if d[i][k] + d[k][j] < d[i][j]:
                d[i][j] = d[i][k] + d[k][j]

# print(d)
for i in range(n):
    for j in range(n):
        if d[i][j] == INF:
            d[i][j] = 0
        print(d[i][j], end=' ')
    print()