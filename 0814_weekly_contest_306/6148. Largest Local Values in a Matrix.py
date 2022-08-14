class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        new_grid = [[0] * (n-2) for _ in range(n-2)]

        for r in range(0, n-2):
            for c in range(0, n-2):
                max_num = 1
                for r2 in range(r, r+3):
                    for c2 in range(c, c+3):
                        if grid[r2][c2] >= max_num:
                            max_num = grid[r2][c2]
                new_grid[r][c] = max_num

        return new_grid

