
"""
1st solution.
Used: DFS algortihm
Complexity analysis:
Time: O((N * M))
Memory: O(N * M) in worst case, stack memory
"""

from collections import deque

# 재귀 풀이
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return 0

            grid[i][j] = 0

            # 현재 위치 사이즈 1을 더한 값
            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)

        maxSize = 0
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:  # 1을 발견하면 dfs 시작
                    maxSize = max(maxSize, dfs(i, j))

        return maxSize


# 재귀 풀이 2
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(i, j):
            # 더 이상 땅이 아닌 경우 종료한다.
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != 1:
                return

            grid[i][j] = 0 # 땅일 경우 방문체크

            for k in range(4):  # 동서남북 탐색
                ni, nj = i + dx[k], j + dy[k]
                dfs(ni, nj)


        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        n, m = len(grid), len(grid[0])

        # 문자열로 들어오는 배열을 int로 전환
        for r in range(n):
            for c in range(m):
                grid[r][c] = int(grid[r][c])

        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    # 섬 발견하면 dfs 시작, dfs가 끝나면 섬의 개수를 하나 늘린다.
                    dfs(i, j)
                    count += 1

        return count
