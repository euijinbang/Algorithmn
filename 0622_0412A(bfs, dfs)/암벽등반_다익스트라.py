"""
dp[i][j] : 시작점에서부터 (i, j)로 가는 걸리는 최소 난이도

다익스트라 문제 특징
1. 모든 경로의 난이도는 0 이상의 정수이다.
2. 시작점에서 최소 난이도의 경로로 갱신해나가면 모든 점에서의
최소 난이도가 기록된다.
3. 문제가 한 점에서 특정 점까지의 최소 난이도를 구한다.

"""
from heapq import heappop, heappush

m, n = 5, 6
wall = [
    [0, 1, 1, 1, 0, 0],
    [3, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [2, 1, 1, 1, 1, 1]
]

# 최댓값 : 높이 차의 최대
dp = [[50] * n for _ in range(m)]

# 도착지 및 시작지 찾기
for i in range(m):
    for j in range(n):
        if wall[i][j] == 3:
            e = (i, j)
        if wall[i][j] == 2:
            s = (i, j)


def bfs(x, y):
    pq = [(x, y, 0)]

    while pq:
        r, c, dist = heappop(pq)

        if dp[r][c] <= dist:
            continue

        dp[r][c] = dist

        # 아래로 이동
        for nr in range(r+1, m):
            if wall[nr][c] == 0: continue
            ndist = max(dist, nr - r)
            if ndist >= dp[nr][c]: continue
            heappush(pq, (nr, c, ndist))

        # 위로 이동
        for nr in range(r-1, -1, -1):
            if wall[nr][c] == 0: continue
            ndist = max(dist, r - nr)
            if ndist >= dp[nr][c]: continue
            heappush(pq, (nr, c, ndist))

        # 오른쪽으로 이동
        for nc in range(c+1, n):
            if wall[r][nc] == 0: break
            if dist >= dp[r][nc]: continue
            heappush(pq, (r, nc, dist))

        # 왼쪽으로 이동
        for nc in range(c-1, -1, -1):
            if wall[r][nc] == 0: break
            if dist >= dp[r][nc]: continue
            heappush(pq, (r, nc, dist))


bfs(s[0], s[1])

# 구하고자 하는 것 : 도착 좌표까지 가는 난이도의 최솟값
print(dp[e[0]][e[1]])

