import collections
from collections import deque
import sys
sys.stdin = open("a1.txt")


def bfs(MAP):
    global max_total
    q = deque()
    for i in range(H):
        for j in range(W):
            total = 0
            DATA = [[0]*W for _ in range(H)]
            visited = [[False]*W for _ in range(H)]

            DATA[i][j] = 1
            q.append((i, j))
            total += MAP[i][j]
            visited[i][j] = True
            size = 1

            while q:
                x, y = q.popleft()

                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny]:
                        DATA[nx][ny] = 1
                        size += 1
                        q.append((nx, ny))
                        visited[nx][ny] = True
                        total += MAP[nx][ny]

                        if size == 4:
                            if total >= max_total:
                                max_total = total
                                break

    return max_total


def dfs(MAP, visited, x, y, cost, depth):
    global max_cost

    if depth == 4:
        if cost >= max_cost:
            max_cost = cost
        return

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]

        if (nx < 0 or nx >= H) or (ny < 0 or ny >= W) or visited[nx][ny]:
            continue

        visited[nx][ny] = True
        cost += MAP[nx][ny]
        dfs(MAP, visited, nx, ny, cost, depth + 1)
        visited[nx][ny] = False
        cost -= MAP[nx][ny]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for tc in range(T):
    W, H = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(H)]
    visited = [[False]*W for _ in range(H)]
    max_total = 0
    ans = []
    ans.append(bfs(MAP) ** 2)

    costs = 0
    for i in range(H):
        for j in range(W):
            # 비용 및 최대비용, visited 초기화
            max_cost = 0
            visited = [[False]*W for _ in range(H)]
            dfs(MAP, visited, i, j, MAP[i][j], 1)
            if costs < max_cost:
                costs = max_cost
    ans.append(costs ** 2)

    print("#{} {}".format(tc+1, max(ans)))




# (Runtime error)
# Error Message:
# Traceback (most recent call last):
# File "main.py", line 62, in <module>
# T = int(input())
# ValueError: invalid literal for int() with base 10: 'from collections import deque


ㅂ