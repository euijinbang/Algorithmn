from collections import deque

n = 5

board = [
    ['A', 0, 0, 0, 0],
    ['A', 'A', 'A', 0, 0],
    ['A', 0, 0, 0, 0],
    [0, 0, 0, 'B', 'B'],
    [0, 0, 0, 0, 'B']
]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * n for _ in range(n)]


def bfs(board, visited):
    q = deque()
    for i in range(n):
        for j in range(n):
            # 시작 섬의 좌표를 모두 담는다.
            if board[i][j] == 'A':
                q.append((i, j))
                visited[i][j] = True
                board[i][j] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
                if board[nx][ny] == 'B':
                    return board[x][y] + 1
                board[nx][ny] = board[x][y] + 1


print(bfs(board, visited))
