from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #1을 발견하면 섬 하나 추가, bfs 진행, 0으로 바꾼다.

        m, n = len(grid), len(grid[0])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        maxArea = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    grid[r][c] = 0      #시작점도 침몰시켜야.
                    area = 0
                    q = deque([(r, c)])
                    while q:
                        x, y = q.popleft()
                        area += 1
                        for d in range(4):
                            nx, ny = x + dx[d], y + dy[d]
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                                grid[nx][ny] = 0
                                q.append((nx, ny))

                    maxArea = max(maxArea, area)
        return maxArea
