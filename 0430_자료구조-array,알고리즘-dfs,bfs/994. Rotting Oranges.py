from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 썩은오렌지 큐에 다 담고 bfs 시작, fresh 개수 반영
        # 비어있는 grid면 -1 반환
        # 다 돌고 fresh가 남아있다면 -1 반환

        m, n = len(grid), len(grid[0])
        if m == 0: return -1

        fresh_cnt = 0
        rotten = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                if grid[r][c] == 1:
                    fresh_cnt += 1      #fresh 갯수를 파악

        di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
        minutes_passed = 0
        while rotten and fresh_cnt:    #fresh가 없는 경우를 제외해야!!
            minutes_passed += 1
            for _ in range(len(rotten)):
                i, j = rotten.popleft()
                for d in range(4):
                    ni, nj = i + di[d], j + dj[d]
                    if 0 <= ni < m and 0 <= nj < n:
                        if grid[ni][nj] == 1:
                            grid[ni][nj] = 2
                            rotten.append((ni, nj))
                            fresh_cnt -= 1

        return minutes_passed if not fresh_cnt else -1
