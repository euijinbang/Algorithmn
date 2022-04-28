from collections import deque

"""
섬의 둘레 구하기
"""
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # n <= 100

        n, m = len(grid), len(grid[0])

        # 섬의 갯수 x 4 - (겹치는 선의 갯수) x 2
        islandCnt = 0
        both = 0

        # 방문여부
        visited = [[0] * m for _ in range(n)]

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    islandCnt += 1
                    visited[i][j] = 1

                    # 방문했다면 카운트하지 않는다.
                    for k in range(4):
                        ni, nj = i + dx[k], j + dy[k]
                        if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                            if grid[ni][nj] == 1:
                                both += 1

        result = islandCnt * 4 - both * 2
        return result
