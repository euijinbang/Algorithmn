def solution(N, jump):
    # 우, 하, 좌, 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    direction = 0
    arr = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    visited[0][0] = 1
    r = 0
    c = 0
    value = 1
    arr[r][c] = value
    state = 0

    while value < N * N:

        # 달팽이의 중앙에 도착하면 다시 최 좌측 상단(0, 0)으로 이동
        if N % 2:  # N이 홀수면 중앙 좌표가 (N//2, N//2)
            if (r, c) == (N // 2, N // 2):
                r, c = 0, 0
                visited = [[0] * N for _ in range(N)]
                visited[0][0] = 1
        else:  # N이 짝수면 중앙 좌표가 (N//2, N//2 - 1)
            if (r, c) == (N // 2, N // 2 - 1):
                r, c = 0, 0
                visited = [[0] * N for _ in range(N)]
                visited[0][0] = 1

        nr = r + dr[direction]
        nc = c + dc[direction]

        # 범위를 벗어나거나 이미 지나온 경로면 방향 전환
        if nr < 0 or nr >= N or nc < 0 or nc >= N or visited[nr][nc]:
            direction = (direction + 1) % 4
            nr = r + dr[direction]
            nc = c + dc[direction]

        visited[nr][nc] = 1

        # 비어있는 곳을 지나면 state 1씩 채우기
        if not arr[nr][nc]:
            state += 1

        # state와 jump가 같아질 때마다 해당 위치에 value를 저장
        # 비어있는 칸을 jump 개씩 건너뛰면서 값 채우기
        if state == jump:
            value += 1
            arr[nr][nc] = value
            state = 0
        r, c = nr, nc

    for i in range(N):
        for j in range(N):
            if arr[i][j] == N * N:
                return [i + 1, j + 1]