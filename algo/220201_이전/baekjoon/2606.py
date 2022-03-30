import sys
sys.stdin = open("2606.txt")

n = int(input()) # 컴퓨터의 수
m = int(input()) # 컴퓨터 쌍의 수

from collections import deque

def dfs(v):
    visited[v] = 1
    for w in adj[v]:
        if not visited[w]:
            dfs(w)
    return visited

def bfs(v):
    q = deque([v])
    visited[v] = 1
    while q:
        v = q.popleft()
        for w in adj[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = 1
    return visited

adj = [[] for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

visited = [0]*(n+1)
result = dfs(1)
cnt = 0
for e in result:
    if e == 1:
        cnt += 1

print(cnt-1) # 1번컴퓨터 제외


