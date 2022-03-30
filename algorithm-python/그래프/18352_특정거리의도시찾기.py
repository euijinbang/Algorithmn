"""
bfs
특정 거리의 도시 찾기
---
시간초과 해결
1. input() 대신 sys.stdin.readline() 사용
2. q = deque([X])
"""
"""
data
1 2
1 3
2 3
2 4
"""
from collections import deque
import sys

N, M, K, X = map(int, sys.stdin.readline().split())

# 인접리스트 생성
graph = [[] for _ in range(N + 1)]
for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)

# 모든 도시에 대한 최단거리 초기화
distance = [-1] * (N + 1)
distance[X] = 0

# 큐 생성하고 시작점 입력
q = deque([X])  #=> 시간초과 방지용

while q:
    now = q.popleft()

    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

flag = False
for i in range(1, N + 1):
    if distance[i] == K:
        print(i)
        flag = True

if not flag:
    print(-1)
