class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '0':
                return
            grid[x][y] = '0'
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                dfs(nx, ny)

        count, m, n = 0, len(grid), len(grid[0])
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1

        return count