class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        b = board
        m, n = len(b), len(b[0])

        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

        def capture(r, c):
            if r < 0 or r == m or c < 0 or c == n or b[r][c] != "O":
                return

            b[r][c] = "T"
            capture(r+1, c)
            capture(r-1, c)
            capture(r, c+1)
            capture(r, c-1)

        # 1. (DFS) Capture unsurrouned regions ("O"->"T")
        for r in range(m):
            for c in range(n):
                if b[r][c] == "O" and (r in [0, m-1] or c in [0, n-1]):
                    capture(r, c)

        # 2. Capture surrouned regions ("O"->"X")
        for r in range(m):
            for c in range(n):
                if b[r][c] == "O":
                    b[r][c] = "X"

        # 3. Unapture unsurrouned regions ("T"->"O")
        for r in range(m):
            for c in range(n):
                if b[r][c] == "T":
                    b[r][c] = "O"
