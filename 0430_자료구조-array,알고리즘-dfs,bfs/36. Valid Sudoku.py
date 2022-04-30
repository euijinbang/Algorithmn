# 방법1. hashSet을 활용한다. 작은 사각형으로 나누어 검사한다.(대박)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r] or
                        board[r][c] in cols[c] or
                        board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True


# 방법2. 행 열 및 작은사각형, 각각 체크한다.
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def makeNewMap():
            numFreq = {}
            for i in range(1, 10):
                numFreq[str(i)] = 0
            return numFreq

        def checkDup(freq):
            for val in nf.values():
                if val >= 2:
                    return False
            return True

        for i in range(9):
            nf = makeNewMap()
            for j in range(9):
                if board[i][j] != '.':
                    nf[board[i][j]] += 1

            if not checkDup(nf):
                return False

        for i in range(9):
            nf = makeNewMap()
            for j in range(9):
                if board[j][i] != '.':
                    nf[board[j][i]] += 1

            if not checkDup(nf):
                return False

        for r in range(3):
            for c in range(3):
                nf = makeNewMap()
                for i in range(3*r, 3*r+3):
                    for j in range(3*c, 3*c+3):
                        if board[i][j] != '.':
                            nf[board[i][j]] += 1

                if not checkDup(nf):
                    return False

        return True
