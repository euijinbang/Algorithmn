from collections import deque
"""
i, j, r, c, k 변수 겹치지 않게 주의할 것. 디버깅이 어렵다.
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # 문자열로 들어오는 배열을 다시 int로 전환

        islandCnt = 0

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        n, m = len(grid), len(grid[0])

        # 변수 겹치지 않게 주의할 것!
        for r in range(n):
            for c in range(m):
                grid[r][c] = int(grid[r][c])

        visited = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    # bfs 시작
                    q = deque()
                    q.append((i, j))

                    islandCnt += 1

                    while q:
                        x, y = q.popleft()
                        # 섬 침몰
                        grid[x][y] = 0
                        visited[i][j] = 1

                        for k in range(4):
                            nx, ny = x + dx[k], y + dy[k]
                            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                                if grid[nx][ny] == 1:
                                    grid[nx][ny] = 0
                                    visited[nx][ny] = 1
                                    q.append((nx, ny))


        return islandCnt
numIslands(grid)