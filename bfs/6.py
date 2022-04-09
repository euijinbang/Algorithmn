from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n = 4
visited = [[False] * n for _ in range(n)]

board = [
    ['A', 0, 0, 'C'],
    [0, 1, 0, 1],
    [0, 1, 0, 1],
    [0, 0, 0, 'B']
]


def bfs(board, visited, S, E):
    for i in range(n):
        for j in range(n):
            if board[i][j] == S:
                start = (i, j)

    # 시작점 세팅
    board[start[0]][start[1]] = 0
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                # 종료조건
                if board[nx][ny] == E:
                    return board[x][y] + 1
                # 전진조건
                if board[nx][ny] == 0:
                    board[nx][ny] = board[x][y] + 1
                    visited[nx][ny] = True
                    q.append((nx, ny))


step1 = bfs(board, visited, 'A', 'B')
# visited 배열 및 배열 초기화
visited = [[False] * n for _ in range(n)]
board = [
    ['A', 0, 0, 'C'],
    [0, 1, 0, 1],
    [0, 1, 0, 1],
    [0, 0, 0, 'B']
]
step2 = bfs(board, visited, 'B', 'C')
print(step1 + step2)
