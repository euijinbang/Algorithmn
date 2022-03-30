n, m = 4, 4     # n 행 m 열

# 방문위치 저장위해 0 초기화
visited = [[0] * m for _ in range(n)]

x, y, d = 1, 1, 0
visited[x][y] = 1   # 현좌표 방문처리

# arr = []
# for i in range(n):
#     arr.append(list(map(int, input().split())))

arr = [
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 0, 0, 1],
    [1, 1, 1, 1],
]

# 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]

    # 회전한 이후 정면에 가보지 않은 칸이 존재한다면 전진한다.
    if arr[nx][ny] == 0 and visited[nx][ny] == 0:
        x = nx
        y = ny
        visited[nx][ny] = 1  #방문체크
        count += 1
        turn_time = 0   #회전수 초기화

    else:   # 회전한 이후 정면이 가봤거나 바다라면
        turn_time += 1   # 회전만 수행하고 처음으로 돌아간다.

    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        # 뒤로 갈 수 있다면 후진한다
        if arr[nx][ny] == 0 and visited[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다라면 멈춘다
        else:
            break
        turn_time = 0 # 회전수 초기화

print(count)