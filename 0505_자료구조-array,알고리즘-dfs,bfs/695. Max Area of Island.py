# dfs
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        global size
        #1을 발견하면 섬 하나 추가, bfs or dfs 진행, 0으로 바꾼다.
        def dfs(x, y):
            global size
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                return
            grid[x][y] = 0
            size += 1
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                dfs(nx, ny)

        m, n, max_size = len(grid), len(grid[0]), 0
        dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    size = 0
                    dfs(i, j)
                    max_size = max(size, max_size)

        return max_size

# global 미사용
def dfs(i,j,grid):

    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == 0:
        return 0

    grid[i][j] = 0

    up = dfs(i,j+1,grid)
    down = dfs(i,j-1,grid)
    left = dfs(i-1,j,grid)
    right = dfs(i+1,j,grid)

    return up + down + left + right + 1

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):

                if grid[i][j] == 1:
                    count = max(dfs(i,j,grid), count)

        return count

# bfs
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
