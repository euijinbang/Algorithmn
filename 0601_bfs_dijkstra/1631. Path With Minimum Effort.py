class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        dijkstra

        1. 최대값으로 채운 거리용 배열, pq, visited 세팅
        2. 조건 : 만약 거리용 배열이 new_w보다 클 때에만!!!! new_w로 갱신한다.
        """
        m, n = len(heights), len(heights[0])
        dst = (m-1, n-1)

        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        costs = [[float('inf')]*n for _ in range(m)] # 최대값으로 배열을 채운다.

        pq = [(0, 0, 0)]  # w, sx, sy
        visited = set()

        while pq:
            w, x, y = heapq.heappop(pq)
            visited.add((x, y))

            if (x, y) == dst:
                return w

            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if 0<=nx<m and 0<=ny<n and (nx,ny) not in visited:
                    new_w = max(w, abs(heights[nx][ny] - heights[x][y]))
                    if costs[nx][ny] > new_w:
                        costs[nx][ny] = new_w
                        heapq.heappush(pq, (new_w, nx, ny))

        return -1