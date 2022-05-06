from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        def bfs(x, y, count, flag):
            #초기설정부분
            q = deque([(x, y)])
            grid[x][y] = 0

            while q:
                x, y = q.popleft()
                count += 1
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    #한번이라도 밖으로 나갔으면 표시해두고 0을 리턴, 아니면 전체 카운트 리턴
                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        flag = False
                        continue
                    if grid[nx][ny] == 0:
                        continue
                    grid[nx][ny] = 0
                    q.append((nx, ny))
            return count if flag else 0


        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
        m, n = len(grid), len(grid[0])
        total_cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    total_cnt += bfs(i, j, 0, True)

        return total_cnt