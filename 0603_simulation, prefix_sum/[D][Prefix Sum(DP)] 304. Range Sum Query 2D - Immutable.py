class NumMatrix:
    """
    # matrix
    1 2 3 4
    5 6 7 8
    9 10 11 12

    # prefix(row-only)
    1 3 6 10
    5 11 18 26
    9 19 30 42
    13 27 42 58

    # dp(prefix-row and column)
    0 0 0 0 0
    0 1 3 6 10
    0 6 14 24 36
    0 15 33 54 78
    0 28 60 96 136

    (r1, c1) ~ (r2, c2) 까지의 합
    = sum((0,0)~(r2,c2))
     -sum((0,0)~(r1-1,c2)
     -sum((0,0)~(r2,c1-1))
     +sum((0,0)~(r1-1,c1-1)))
    """

    def __init__(self, matrix: List[List[int]]):
        row, col = len(matrix), len(matrix[0])
        self.dp = [[0] * (col+1) for _ in range(row+1)]

        for r in range(row):
            prefix = 0
            for c in range(col):
                prefix += matrix[r][c]
                above = self.dp[r][c+1]
                self.dp[r+1][c+1] = above + prefix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        bottom_right = self.dp[row2][col2]
        above = self.dp[row1-1][col2]
        left = self.dp[row2][col1-1]
        left_above = self.dp[row1-1][col1-1]

        return bottom_right - above - left + left_above
