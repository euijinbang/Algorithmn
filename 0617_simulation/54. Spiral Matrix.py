class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우하좌상
        m, n = len(matrix), len(matrix[0])
        result = []

        d = 0
        r = c = 0

        while len(visited) < m * n:

            result.append(matrix[r][c])
            visited.add((r, c))

            nr, nc = dirs[d][0] + r, dirs[d][1] + c

            if nr < 0 or nr >= m or nc < 0 or nc >= n or (nr, nc) in visited:
                d = (d + 1) % 4
                nr, nc = dirs[d][0] + r, dirs[d][1] + c

            r, c = nr, nc

        return result
