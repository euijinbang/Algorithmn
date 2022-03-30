
# n = 6
# vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
from collections import deque

n = int(input())
vertex = input()

def bfs(v):
    q = deque([v])
    visited[v] = 1

    while q:
        v = q.popleft()
        for w in adj[v]:
            if visited[w] == 0:
                visited[w] = visited[v] + 1
                q.append(w)

    return visited

adj = [[] for _ in range(n+1)]
for i in range(n):
    x, y = vertex[i][0], vertex[i][1]
    adj[x].append(y)
    adj[y].append(x)

visited = [0] * (n+1)
result = max(bfs(1))
print(result)






