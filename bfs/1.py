from collections import deque

# 좌표 == 노드
# 동서남북 탐색 == 노드에 다리가 4개 연결되어 있는 것

n = 4
board = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(board, start, visited):
    q = deque()
    # 시작점 큐에 넣고 방문체크
    q.append(start)
    visited[start[0]][start[1]] = True

    while q:
        x, y = q.popleft()

        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                board[nx][ny] = board[x][y] + 1
                q.append([nx, ny])

    return board

start = (1, 1)
visited = [[False] * n for _ in range(n)]

result = bfs(board, start, visited)
for i in range(n):
    print(result[i])
