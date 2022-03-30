n = 5
jump = 3

# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 배열 생성 및 초기화
arr = [[0] * n for _ in range(n)]
value = 1
arr[0][0] = value

# 방문위치 배열 생성 및 초기화
visited = [[0] * n for _ in range(n)]
visited[0][0] = 1

# 시작 좌표
x, y = 0, 0

# 방향
d = 0

# jump 를 세는 변수
state = 0

while value < (n * n):

    # 달팽이 중앙 도착시 다시 최좌측 상단으로 이동한다.
    if n % 2:
        # n 이 홀수면 중앙 좌표는 (n//2, n//2)
        if (x, y) == (n//2, n//2):
            x, y = 0,  0
            visited = [[0] * n for _ in range(n)]
            visited[0][0] = 1
    else:
        # n 이 짝수면 중앙 좌표는 (n//2, n//2-1)
        if (x, y) == (n//2, n//2-1):
            x, y = 0,  0
            visited = [[0] * n for _ in range(n)]
            visited[0][0] = 1

    # 다음 좌표 설정 (이부분이 위 조건 위로 가면 무한루프 돈다)
    nx = x + dx[d]
    ny = y + dy[d]

    # 좌표를 넘어가거나 이미 지나온 경로면 방향을 전환한다.
    if nx < 0 or ny < 0 or nx >= n or ny >= n or visited[nx][ny]:

        # 방향전환하고 좌표를 재설정한다.
        d = (d + 1) % 4
        nx = x + dx[d]
        ny = y + dy[d]

    # 방문체크한다.
    visited[nx][ny] = 1

    # 빈 곳을 지나면 state를 1씩 채운다.
    if not arr[nx][ny]:
        state += 1

    # state와 jump가 같아질 때 마다 해당 위치에 value 를 저장한다.
    if state == jump:
        value += 1
        arr[nx][ny] = value
        state = 0

    # 모든 처리 끝내고 마지막에 전진
    x, y = nx, ny

print(arr)

# 좌표 밸류값이 n*n 인 곳의 좌표를 반환한다.
for i in range(n):
    for j in range(n):
        if arr[i][j] == n * n:
            print([i+1, j+1])


