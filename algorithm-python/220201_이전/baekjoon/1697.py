# 특정 위치까지 이동하는 최단시간을 구하는 문제
import sys
sys.stdin = open("1697.txt")


from collections import deque

MAX = 100001
n, k = map(int, input().split())
visited = [0] * MAX

def bfs():
    def a(x):
        return x - 1

    def b(x):
        return x + 1

    def c(x):
        return 2 * x

    q = deque([n])
    while q:
        s = q.popleft()

        if s == k:
            # print(visited)
            return visited[s]

        if 0 <= a(s) < MAX and visited[a(s)] == 0:
            q.append(a(s))
            visited[a(s)] = visited[s] + 1
        if 0 <= b(s) < MAX and visited[b(s)] == 0:
            q.append(b(s))
            visited[b(s)] = visited[s] + 1
        if 0 <= c(s) < MAX and visited[c(s)] == 0:
            q.append(c(s))
            visited[c(s)] = visited[s] + 1

print(bfs())



