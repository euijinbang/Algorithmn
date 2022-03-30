import sys
sys.stdin = open("1260.txt")

from collections import deque
N, M, V = map(int, input().split())


def dfs(v):
    dfs = []
    stack = [v]
    while stack:
        v = stack.pop()
        # 이미 방문한경우 출력하지 않는다 ㅠㅠ
        if visited[v] == 0:
            dfs.append(v)
        visited[v] = 1
        for w in sorted(adjList[v], reverse=True):
            if visited[w] == 0 :
                stack.append(w)

    return dfs


def bfs(v):
    bfs = []
    queue = deque([v])
    while queue:
        v = queue.popleft()  # 현재 정점. deque popleft 메서드 사용
        if visited[v] == 0:
            visited[v] = 1
            bfs.append(v)
        for w in adjList[v]:
            if visited[w] == 0:
                queue.append(w)

    return bfs

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
print(" ".join(map(str, dfs(V))))
# print(adjList)
visited = [0] *(N+1)
print(" ".join(map(str, bfs(V))))
