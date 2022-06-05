class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        for문으로 돌기때문에 visited 불필요
        좌측대각선, 우측대각선 각각 r-c, r+c, 유지되는 성질 활용
        backtrack 조건 확인, "."으로 돌리면 되므로 board는 1개만 필요

        row 는 1씩 증가, col 은 0부터 돌리면서 조건에 맞으면 dfs실행

        """
        result = []
        board = [['.'] * n for _ in range(n)]
        col, pos_diag, neg_diag = set(), set(), set()

        def backtrack(r):
            # base case
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)

            for c in range(n):
                if c in col or r+c in pos_diag or r-c in neg_diag:
                    continue

                col.add(c)
                pos_diag.add(r+c)
                neg_diag.add(r-c)
                board[r][c] = 'Q'

                backtrack(r+1)

                col.remove(c)
                pos_diag.remove(r+c)
                neg_diag.remove(r-c)
                board[r][c] = '.'

        backtrack(0)

        return result
