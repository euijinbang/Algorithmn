import sys
sys.stdin = open("1260.txt")

from collections import deque
N, M, V = map(int, input().split())


def dfs(v):
    # dfs는 스택에 넣고 시작, 빼면서 방문처리
    stack = [v]
    while stack:
        v = stack.pop()
        if visited[v] == 0:
            print(v, end=' ')
        visited[v] = 1
        # for w in adjList[v]:
        for w in sorted(adjList[v], reverse=True):
            if visited[w] == 0 and w not in stack:
                stack.append(w)

def dfs2(v):
    # 재귀의 경우 시작점부터 연결노드를 돌면서 방문처리
    print(v, end=' ')
    visited[v] = 1
    for w in adjList[v]:
        if visited[w] == 0:
            dfs2(w)

def bfs(v):
    # bfs는 방문표시하고 큐에 넣고 시작
    visited[v] = 1
    queue = deque([v])
    print(v, end=' ')
    while queue:
        v = queue.popleft()
        for w in adjList[v]:
            if visited[w] == 0:
                # 방문처리하고 큐에 넣는다
               visited[w] = 1
               queue.append(w)
               print(w, end=' ')

# 인접행렬
# adj = [[0]*(N+1) for _ in range(N+1)]
# for i in range(M):
#     n1, n2 = map(int, input().split())
#     adj[n1][n2] = 1
#     adj[n2][n1] = 1

# 인접리스트
adjList = [[] for _ in range(N+1)]
for i in range(M):
    n1, n2 = map(int, input().split())
    adjList[n1].append(n2)
    adjList[n2].append(n1)

# 정점번호가 작은것부터 방문하기 위해 인접리스트를 소트
for e in adjList:
    e.sort()


# visited 초기화
visited = [0]*(N+1)
dfs(V)
print()
visited = [0] *(N+1)
bfs(V)

