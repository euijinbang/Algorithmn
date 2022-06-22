"""
DP + 다익스트라
또는 BFS (우선순위큐 느낌을 곁들인..)

난이도 1~최대높이로 낮은 난이도부터 시작해서
도착지에 도달하면 멈춘다.
"""

m, n = 5, 6
wall = [
    [0, 1, 1, 1, 0, 0],
    [3, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [2, 1, 1, 1, 1, 1]
]

# 도착지 및 시작지 찾기
for i in range(m):
    for j in range(n):
        if wall[i][j] == 3:
            e = (i, j)
        if wall[i][j] == 2:
            s = (i, j)

# 골인지점까지 도달할 때 이동했던 최대 높이가 난이도이므로
# 낮은 난이도부터 갈 수 있는지 차례로 확인한다.
hard = 1
while hard < m:
    stack = [s]
    visited = set()
    # bfs
    while stack:
        ci, cj = stack.pop()
        visited.add((ci, cj))
        # 델타 탐색
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            # 수직으로 갈 수 있는 높이는 1~난이도
            # 갈 수 있는 범위를 모두 탐색
            for h in range(1, hard + 1):
                ni = ci + di * h
                nj = cj + dj

                # 방문하지 않았고 그 위치가 돌이라면 스택에 추가한다.
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
                    if wall[ni][nj] == 1 or wall[ni][nj] == 3:
                        stack.append((ni, nj))

    # 도착지점에 방문했다면
    if e in visited:
        break

    # 도착 못했다면 난이도를 1 높여서 반복한다.
    hard += 1

print(hard)

