from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        maxSize = 0
        m, n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)]
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:  # 1을 발견하면 bfs 시작

                    q.append((i, j))
                    visited[i][j] = 1
                    size = 1

                    while q:
                        x, y = q.popleft()

                        for k in range(4):
                            nx, ny = x + dx[k], y + dy[k]
                            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                                if grid[nx][ny] == 1:
                                    visited[nx][ny] = 1
                                    q.append((nx, ny))
                                    size += 1

                    maxSize = max(maxSize, size)

        return maxSize