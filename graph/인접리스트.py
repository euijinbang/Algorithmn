from collections import deque

n = 6
m = 7
graph = [[] for _ in range(n+1)]

# 단방향
# for i in range(m):
#     start, end = map(int, input().split())
#     graph[start].append(end)

# 양방향
# for i in range(m):
#     start, end = map(int, input().split())
#     graph[start].append(end)
#     graph[end].append(start)

visited = [False] * (n+1)

route_bfs = []
def bfs(graph):
    q = deque()
    q.append(1)
    visited[1] = True

    while q:
        now = q.popleft()
        route_bfs.append(now)
        for next in graph[now]:
            if not visited[next]:
                q.append(next)
                visited[next] = True

    return route_bfs

route_dfs = []
def dfs(graph):
    q = deque()
    q.append(1)
    visited[1] = True

    while q:
        now = q.pop()
        route_dfs.append(now)
        for next in graph[now]:
            if not visited[next]:
                q.append(next)
                visited[next] = True

    return route_dfs

route_dfs2 = []
def dfs2(graph, v):
    route_dfs2.append(v)
    visited[v] = True

    for next in graph[v]:
        if not visited[next]:
            dfs2(graph, next)

    return route_dfs2


# print(bfs([[], [2, 5], [1, 3, 5], [2, 4], [3, 6], [1, 2, 6], [5, 4]]))
# print(dfs([[], [2, 5], [1, 3, 5], [2, 4], [3, 6], [1, 2, 6], [5, 4]]))
print(dfs2([[], [2, 5], [1, 3, 5], [2, 4], [3, 6], [1, 2, 6], [5, 4]], 1))
# [[], [2], [3], [4], [], [1, 2, 6], [4]]
# [[], [2, 5], [1, 3, 5], [2, 4], [3, 6], [1, 2, 6], [5, 4]]