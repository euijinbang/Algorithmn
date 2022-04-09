from collections import deque

board = [
    [0, 1, 0, 0],
    [3, 1, 2, 2],
    [0, 1, 0, 2],
    [0, 1, 0, 2],
    [0, 0, 0, 0]
]

start = (0, 1)

# 사람은 3 - 1은 벽 - 섬에 도착하는 최소 거리? 6
# 3분..10분걸리면 문제있다

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited = [[0] * 4 for _ in range(4)]

    while q:
        x, y = q.popleft()
        step = board[x][y]

        if step == 2:
            return

        for dir in direction
