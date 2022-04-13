from collections import deque

n, m = 6, 4

board = [[0, 1, 0, 0],
         [3, 1, 2, 2],
         [0, 1, 0, 2],
         [0, 1, 0, 2],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * m for _ in range(n)]
count = 0


def bfs(board, visited, count):
    q = deque()
    for i in range(n):
        for j in range(m):
            if board[i][j] == 3:
                start = (i, j)
                # 시작점 설정
                q.append(start)
                visited[i][j] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
                count += 1
                # 발견하자 마자 종료
                if board[nx][ny] == 2:
                    return count


print(bfs(board, visited, count))
