class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        global flag
        def dfs(x, y):
            global flag

            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 1 or grid[x][y] == 2:
                if x < 0 or x >= m or y < 0 or y >= n:
                    flag = False
                return

            grid[x][y] = 2 #방문처리

            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                dfs(nx, ny)

        m, n, count = len(grid), len(grid[0]), 0
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    flag = True
                    dfs(i, j)
                    if flag:
                        count += 1

        return count


############################################################

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            # 맵 밖으로 나가면 고립된 섬이 아니다.
            if i < 0 or i >= m or j < 0 or j >= n:
                return False

            # 1이면 벽이므로 True를 리턴한다.
            if grid[i][j] == 1:
                return True

            # 방문체크
            grid[i][j] = 1

            up = dfs(i - 1, j)
            down = dfs(i + 1, j)
            left = dfs(i, j - 1)
            right = dfs(i, j + 1)

            return up and down and left and right

        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    if dfs(r, c):
                        count += 1

        return count