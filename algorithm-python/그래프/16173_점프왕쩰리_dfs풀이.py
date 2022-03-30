# N = int(input())
# m = [list(map(int, input().split())) for _ in range(N)]

N = 3
m = [
    [1, 1, 10],
    [1, 5, 1],
    [2, 2, -1]
]

from collections import deque

def solution(N, m):
    visit = [[0] * N for _ in range(N)]
    dx = [1, 0]
    dy = [0, 1]
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.pop()
        if m[x][y] == -1:
            return True

        for i in range(2):
            nx = x + dx[i] * m[x][y]
            ny = y + dy[i] * m[x][y]
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0:
                q.append((nx, ny))
                visit[nx][ny] = 1


if solution(N, m):
    print('HaruHaru')
else:
    print('Hing')