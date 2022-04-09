from collections import deque

n = 5
board = [[0, 1, 1, 1, 0],
         [0, 1, 0, 0, 1],
         [0, 1, 0, 0, 1],
         [0, 1, 1, 1, 0],
         [1, 0, 0, 1, 0]]
visited = [[False] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0


def bfs(board, visited, count):
    q = deque()
    # 이중for 문 돌려서 나올 때 마다 침몰
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                count += 1
                q.append((i, j))
                board[i][j] = 0

                while q:
                    x, y = q.popleft()
                    for i in range(4):
                        nx, ny = x + dx[i], y + dy[i]
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                            # 4방향 중 특정 노드를 방문하는 조건을 추가
                            if board[nx][ny] == 1:
                                visited[nx][ny] = True
                                # 섬을 침몰시킨다
                                board[nx][ny] = 0
                                q.append((nx, ny))

    return count

result = bfs(board, visited, count)
print(result)
