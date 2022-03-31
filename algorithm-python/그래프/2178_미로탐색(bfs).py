from collections import deque

"""
최단경로 == bfs! 가장 마지막 좌표를 기준으로 다음 좌표를 구하며
최단경로를 구해야 하기 때문에 bfs가 적절하다.
dfs 는 갈 수 있는 끝까지 가기때문에 count 수가 계속 증가한다. (빼주지 않는 이상)
bfs 돌면서 1이면 이동하며 +1씩 더해
도착점의 value 를 출력한다.
"""

# N, M = 4, 6
# board = [
#     [1, 0, 1, 1, 1, 1],
#     [1, 0, 1, 0, 1, 0],
#     [1, 0, 1, 0, 1, 1],
#     [1, 1, 1, 0, 1, 1]
# ]

N, M = map(int, input().split())
board = []

for i in range(N):
    board.append(list(map(int, input())))  # 공백 없이 들어오는 데이터

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):

    # deque 생성
    q = deque()
    q.append((x, y))

    while q:
        # 현재 위치
        x, y = q.popleft()

        # 현재 위치에서 4가지 방향으로 위치 확인
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            # 위치를 벗어나면 안되므로 조건 추가
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 벽이므로 진행 불가
            if board[nx][ny] == 0:
                continue

            # 벽이 아니므로 이동
            if board[nx][ny] == 1:
                board[nx][ny] = board[x][y] + 1
                q.append((nx, ny))

    # 마지막 값에서 카운트 값을 뽑는다.
    return board[N-1][M-1]


print(bfs(0, 0))

