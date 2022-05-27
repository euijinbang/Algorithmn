class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])

        def dfs(x, y):
            if x < 0 or x == m or y < 0 or y == n or board[x][y] != "X" :
                return

            board[x][y] = "."
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)

        # 좌표 돌면서 X 발견시 dfs 실행
        cnt = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    dfs(i, j)
                    cnt += 1

        return cnt