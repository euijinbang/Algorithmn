class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        N = 3
        rows, cols = [0] * N, [0] * N
        mainDiag = antiDiag = 0

        player = 1
        for r, c in moves:
            rows[r] += player
            cols[c] += player
            if r == c: mainDiag += player
            if r + c == N - 1: antiDiag += player
            if abs(rows[r]) == N or abs(cols[c]) == N or abs(mainDiag) == N or abs(antiDiag) == N:
                return "A" if player == 1 else "B"
            player = -player

        return "Draw" if len(moves) == N * N else "Pending"



class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:

        board = [[""]*3 for _ in range(3)]

        result = {
            "XXX" : "A",
            "OOO" : "B"
        }

        for i, (r, c) in enumerate(moves):
            if not i % 2:
                board[r][c] = "X"
            else:
                board[r][c] = "O"

        diag_l, diag_r = [], []
        for r in range(3):
            diag_l.append(board[r][r])
            diag_r.append(board[r][2-r])

            if "".join(board[r]) in result:
                return result["".join(board[r])]

            col = []
            for c in range(3):
                col.append(board[c][r])

            if "".join(col) in result:
                return result["".join(col)]

        if "".join(diag_l) in result:
            return result["".join(diag_l)]

        if "".join(diag_r) in result:
            return result["".join(diag_r)]

        return "Draw" if len(moves) == 9 else "Pending"

