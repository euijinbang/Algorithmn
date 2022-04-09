from collections import deque

N, M = 5, 4
board = [['A', 0, 0, 0],
         [0, 1, 0, 0],
         [0, 1, 'B', 0],
         [0, 1, 1, 0],
         [0, 0, 0, 0]]

visited = [[False] * M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(board, visited):
    q = deque()
    # 시작점 찾기
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'A':
                q.append((i, j))
                visited[i][j] = True
                board[i][j] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                # 종료조건
                if board[nx][ny] == 'B':
                    result = board[x][y] + 1
                    return result

                if board[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    board[nx][ny] = board[x][y] + 1


print(bfs(board, visited))



