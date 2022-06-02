class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        dijkstra
        1. 최대값으로 채운 거리용 이차원 배열, pq, visited 세팅
        2. new_w(이전 노드까지의 max effort 와 현 노드 effort 중 더 큰 값)
        가 costs배열보다 작으면 new_w로 갱신한다.
        """

        m, n = len(heights), len(heights[0])
        dst = (m-1, n-1)

        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        costs = [[float('inf')]*n for _ in range(m)]  # 최대값으로 배열을 채운다.

        pq = [(0, 0, 0)]  # w, sx, sy
        visited = set()

        while pq:
            w, x, y = heapq.heappop(pq)
            visited.add((x, y))

            if (x, y) == dst:
                return w

            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    new_w = max(w, abs(heights[nx][ny] - heights[x][y]))
                    if new_w < costs[nx][ny]:
                        costs[nx][ny] = new_w
                        heapq.heappush(pq, (new_w, nx, ny))

        return -1
