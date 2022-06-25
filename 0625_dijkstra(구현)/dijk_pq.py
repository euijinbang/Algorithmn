"""
A(0,0) 에서 B, C, D, E 로 가는 각각의 최단 경로 구하기
"""
import heapq

MAX = 9999
N = 5
graph = [
    [MAX, 3, MAX, 9, 5],
    [MAX, MAX, 7, MAX, 1],
    [MAX, MAX, MAX, 1, MAX],
    [MAX, MAX, MAX, MAX, MAX],
    [MAX, MAX, 1, MAX, MAX]
]

visited = set()

adj_list = [] * N
for i in range(N):
    adj_row = []
    for j in range(N):
        if graph[i][j] != MAX:
            adj_row.append((graph[i][j], j))  # 비용, 도착점
    adj_list.append(adj_row)

# 시작점에서 각 지점까지의 비용
result = [MAX] * N

min_heap = [(0, 0)]  # 비용, 시작점
while min_heap:
    time, node_idx = heapq.heappop(min_heap)

    # 꺼낸 지점이 아직 미방문 지점이면
    if node_idx not in visited:
        result[node_idx] = time  # 시작점에서 도착점들까지의 최단거리 배열 갱신

    visited.add(node_idx)  # 가장 비용 적은 지점 꺼내고 방문체크

    if len(visited) == N:
        break

    for adj_time, adj_node_idx in adj_list[node_idx]:  # 연결된 지점 중 방문 안했다면
        if adj_node_idx not in visited:
            # heappush 로 넣으면 작은 순으로 들어간다. 이때 비용은 기존것에서 더해야한다.
            heapq.heappush(min_heap, (time + adj_time, adj_node_idx))


print(result)

