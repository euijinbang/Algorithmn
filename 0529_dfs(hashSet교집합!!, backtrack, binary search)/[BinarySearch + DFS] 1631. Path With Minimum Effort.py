class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        binary search
        threshold를 중간으로 잡고, dfs 돌려서
        (다음 이동 노드까지의 간선비용이 기존 threshold 이하이면 진행)
        도착지점까지 갈수있다면 threshold를 binary search로 줄여나가고,
        못간다면 늘려간다.
        최종적으로 mx 값을 반환한다.
        """
        m, n = len(heights), len(heights[0])
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]


        # dfs
        def dfs(k, x, y):
            visited.add((x, y))

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:

                    # 다음 이동 노드까지의 간선비용이 기존 threshold 이하이면 진행
                    new_k = abs(heights[x][y] - heights[nx][ny])

                    if new_k <= k:
                        dfs(k, nx, ny)


        # binary search
        mn, mx = -1, max(max(heights, key=max))

        while mn + 1 < mx:
            visited = set() # 매번 돌때마다 갱신한다.
            mid = (mn + mx) // 2
            dfs(mid, 0, 0)

            # 다 돌았는데 중간에라도 도착지점에 도착했다면 k를 줄여도 되므로 mx를 줄인다.
            # 다 돌았는데 도착지점에 도착하지 못했다면 k를 늘려야 하므로 mn을 늘린다.

            if (m-1, n-1) in visited:
                mx = mid
            else:
                mn = mid

        # 최종적으로 mx를 반환한다.
        return mx