from collections import deque

N, M = 5, 6
board = [
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
]

# 이동할 네 방향을 정의한다. (상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# BFS 구현
def bfs(x, y):
    # deque 라이브러리 사용하여 큐 구현, 큐에 시작점 넣는다.
    q = deque()
    q.append((x, y))

    # 큐가 빌때까지 반복한다.
    while q:
        # 큐에서 하나의 원소(좌표)를 뽑는다.
        x, y = q.popleft()
        # 그 위치에서 4방향을 확인한다.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로찾기 공간을 벗어난 경우 무시한다.
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 벽인 경우 무시한다.
            if board[nx][ny] == 0:
                continue
            # 해당 노드(다음 위치)를 처음 방문하는 경우 최단거리를 기록하고 큐에 해당위치를 넣는다.
            if board[nx][ny] == 1:
                board[nx][ny] = board[x][y] + 1
                q.append((nx, ny))

    # 가장 오른쪽 아래까지의 최단거리를 반환한다.
    return board[N-1][M-1]

# 수행 결과를 출력한다.
print(bfs(0, 0))
for i in board:
    print(i, ' ')
