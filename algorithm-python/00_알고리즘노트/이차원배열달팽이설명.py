n = 5
jump = 3

# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 배열
arr = [[0] * n for _ in range(n)]

# 시작 좌표
x, y = 0, 0

# 방향
d = 0

for number in range(1, n ** 2 + 1):
    arr[x][y] = number

    nx = x + dx[d]
    ny = y + dy[d]

    # 좌표를 넘어가거나, 가려는 곳에 숫자가 있다면
    if nx < 0 or ny < 0 or nx >= n or ny >= n or arr[nx][ny] != 0:
        # 방향전환한다
        d = (d + 1) % 4

        # 좌표를 다시 이동시킨다
        nx = x + dx[d]
        ny = y + dy[d]

    # 범위를 벗어나지 않았다면 이동한다.
    x = nx
    y = ny

print(arr)


