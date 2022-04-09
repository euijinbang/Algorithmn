# import sys
# sys.stdin = open("14195_input.txt")
from collections import deque

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(board, visited, type, count, max_size):
    """
    미생물 타입 type
    미생물의 개수 count
    미생물의 크기 size
    """
    q = deque()
    for i in range(N):
        for j in range(M):
            if board[i][j] == type:
                count += 1  # 미생물 개수 + 1
                size = 1  # 사이즈 초기화
                # 시작점 세팅
                q.append((i, j))
                board[i][j] = '_'
                visited[i][j] = True

                while q:
                    x, y = q.popleft()

                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                            # 섬을 침몰시킨다
                            if board[nx][ny] == type:
                                q.append((nx, ny))
                                board[nx][ny] = '_'
                                size += 1

                if size > max_size:
                    max_size = size

    return count, max_size


for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N 행 M 열
    board = []
    for i in range(N):
        board.append(list(input()))

    visited = [[0] * M for _ in range(N)]

    temps = [bfs(board, visited, "A", 0, 0), bfs(board, visited, "B", 0, 0)]

    result = [temps[0][0], temps[1][0], max(temps[0][1], temps[1][1])]

    print("#{} {} {} {}".format(tc, result[0], result[1], result[2]))
