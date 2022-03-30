# 2번 문제 풀이

def solution(n, clockwise):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    board = [[0] * n for _ in range(n)]

    # 네 점 각각의 좌표 초기 설정
    rows = [0, 0, n - 1, n - 1]
    cols = [0, n - 1, 0, n - 1]

    # 네 점 각각의 방향 초기 설정, 시기방향/반대방향 변수 설정
    if clockwise:
        directions = [1, 2, 0, 3]
        d_idx = 1
    else:
        directions = [2, 3, 1, 0]
        d_idx = -1

    total_count = n * n // 4 + n % 2  # board에 채워질 최대값

    for count in range(1, total_count + 1):
        for i in range(4):  # 네 점을 돌면서
            r, c, d = rows[i], cols[i], directions[i]
            board[r][c] = count
            nr, nc = r + dr[d], c + dc[d]

            # 현재 방향으로 갈 수 있고, 다른 수가 채워지지 않은 경우 좌표 갱신(전진)
            if 0 <= nr < n and 0 <= nc < n and not board[nr][nc]:
                rows[i], cols[i] = nr, nc
            # 현재 방향으로 더 이상 갈 수 없거나, 이미 다른 수가 채워진 경우 방향 전환
            else:
                d = directions[i] = (d + d_idx) % 4
                rows[i], cols[i] = r + dr[d], c + dc[d]

    return board