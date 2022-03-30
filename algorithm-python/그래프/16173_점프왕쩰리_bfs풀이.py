from collections import deque

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(sx: int, sy: int) -> bool:
    q = deque()
    q.append([sx, sy])

    visited = [[False]*3 for _ in range(n)]

    while q:
        x, y = q.popleft()
        step = maps[x][y]

        if maps[x][y] == -1:
            return True

        for dir in range(4):
            nx, ny = x + dx[dir]*step, y + dy[dir]*step
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx, ny])


if bfs(0, 0):
    print('HaruHaru')
else:
    print('Hing')