class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # arr의 val 바꾸는것보다 set(visited) 가 더 빠르다.

        n = len(grid)

        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1

        q = collections.deque()
        q.append((0, 0, 1))  #x, y, distance
        visited = set()
        dirs = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]

        while q:
            x, y, d = q.popleft()

            if x == n-1 and y == n-1:
                return d

            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) \
                        not in visited:
                    visited.add((nx, ny))
                    q.append((nx, ny, d+1))

        return -1