from collections import deque
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # grid2 돌면서 1이 나오면 bfs 시작, 한 턴 중에 grid1좌표를 매번 검사해서
        # 한 번이라도 0이 나오면 False 를 반환.
        # 계속 돌아야 하기 때문에 return False를 바로 해서는 안된다.
        def bfs(x, y):
            q = deque([(x, y)])
            visited.add((x, y))
            res = True
            while q:
                x, y = q.popleft()
                if grid1[x][y] == 0:
                    res = False

                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                        if grid2[nx][ny] == 1:
                            q.append((nx, ny))
                            visited.add((nx, ny))
            return res


        m, n = len(grid2), len(grid2[0])
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
        cnt = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and (i, j) not in visited and bfs(i, j):
                    print((i, j))
                    cnt += 1

        return cnt