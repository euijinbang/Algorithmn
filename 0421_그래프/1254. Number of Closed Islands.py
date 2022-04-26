"""
1로 둘러쌓인 고립된 섬의 개수는?

0일때 마다 dfs로 확인
1이면 True를 리턴, 맵 밖으로 나가면 False를 리턴(섬이 아니다.)
연결된 모든 노드를 탐색할 때, 하나라도 False 이면 섬이 아니므로
모두 True를 리턴하는 경우 dfs 종료 후 섬의 개수를 하나 추가한다.
"""

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