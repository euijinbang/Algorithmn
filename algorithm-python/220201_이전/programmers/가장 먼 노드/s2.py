from collections import deque

# 디버깅중....
def solution(n, edge):
    visited = [0] * (n + 1)
    adj = [[] for _ in range(n + 1)]
    for i in range(n):
        x, y = edge[i][0], edge[i][1]
        adj[x].append(y)
        adj[y].append(x)

    q = deque([1])
    visited[1] = 1

    while q:
        v = q.popleft()
        for w in adj[v]:
            if visited[w] == 0:
                visited[w] = visited[v] + 1
                q.append(w)

    return ...



vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(6, vertex))





