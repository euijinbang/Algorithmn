from collections import deque

#방법1. 위상정렬과 bfs 풀이
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # 최소거리를 구하기 위해 0으로부터 1을 찾는다.(위상정렬이라 함)
        # 0의 모든 좌표를 큐에 넣고 방문하지 않았다면 이전 위치 + 1로 업데이트한다.

        m, n = len(mat), len(mat[0])
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = -1      # visited 대신 -1이면 미방문 좌표

        while q:
            x, y = q.popleft()
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < m and 0 <= ny < n and mat[nx][ny] == -1:
                    mat[nx][ny] = mat[x][y] + 1
                    q.append((nx, ny))

        return mat

#방법2. DP
#top-left 로 좌표가 1일때 DP실행, 이후 bottom-right 실행하면서 더 작은 값으로 갱신

class Solution:  # 520 ms, faster than 96.50%
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        #top-left
        for r in range(m):
            for c in range(n):
                if mat[r][c] > 0:
                    top = mat[r-1][c] if r > 0 else math.inf
                    left = mat[r][c-1] if c > 0 else math.inf
                    mat[r][c] = min(top, left) + 1

        #bottom-right
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if mat[r][c] > 0:
                    bottom = mat[r+1][c] if r < m-1 else math.inf
                    right = mat[r][c+1] if c < n-1 else math.inf
                    mat[r][c] = min(mat[r][c], bottom + 1, right + 1)

        return mat
