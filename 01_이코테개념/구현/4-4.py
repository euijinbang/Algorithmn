N, M = 4, 4
x, y, d = 1, 1, 0
arr = [
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 0, 0, 1],
    [1, 1, 1, 1],
]

# 북-동-남-서
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

visited = 1
arr[x][y] = 2               # 시작칸 방문체크

turn_time = 0
while True:
    d = (d + 1) % 4

    nx = x + dx[d]
    ny = y + dy[d]

    if arr[nx][ny] == 0:    # 왼쪽 가보지 않았다면 회전 후 전진
        x = nx
        y = ny
        visited += 1
        arr[nx][ny] = 2
        turn_time = 0
    else:
        turn_time += 1
        if arr[nx][ny] == 2:
            continue               # 왼쪽 방향에 가보지 않은 칸이 없다면 회전만 하고 1단계로 이동

    if turn_time == 4:          # 네 방향 모두 이미 가본 칸이거나 바다인 경우
        break

print(visited)
