class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        # 빈 배열 엣지케이스
        if not board:
            return []

        def dfs(r, c):
            # 1. 현 위치가 E 가 아니면 리턴
            if board[r][c] != "E":
                return

            # 2. E 라면 주위 Mine 갯수세기
            mine_count = 0
            directions = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]
            for d in directions:
                nr, nc = r + d[0], c + d[1]
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == "M":
                    mine_count += 1

            # 3. 지뢰가 없으면 B로 변경하고 dfs 진행한다.
            if mine_count == 0:
                board[r][c] = "B"

                for d in directions:
                    nr, nc = r + d[0], c + d[1]
                    if 0 <= nr < m and 0 <= nc < n:
                        dfs(nr, nc)
            # 4. 지뢰가 있으면 그 숫자로 업데이트하고 리턴한다.
            else:
                board[r][c] = str(mine_count)
                return

        m, n = len(board), len(board[0])
        i, j = click[0], click[1]

        # 1. 클릭위치가 지뢰이면 X로 변경 후 게임 종료
        if board[i][j] == "M":
            board[i][j] = "X"
            return board

        # 2. 클릭위치가 지뢰가 아니면 dfs 실행
        dfs(i, j)

        return board
