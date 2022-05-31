# BFS
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        # 0->1을 찾는다
        # 0을 큐에 여러개 넣고 BFS시작 => 자동으로 거리별로 sorting 됨
        """

        m, n = len(mat), len(mat[0])
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]

        # inf 2차원 배열을 만든다.
        dest = [[float('inf')]*n for _ in range(m)]
        q = collections.deque()

        # 1. 0인 좌표는 위치용 좌표에서 0으로 만들고, 0좌표를 모두 큐에 담는다.
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dest[i][j] = 0
                    q.append((i, j))

        # 2. bfs 를 실행한다.
        # 큐에서 pop, 다음 좌표가 현재거리+1보다 크면
        # 새 좌표를 현재거리+1로 업데이트하고 큐에 담는다.
        while q:
            x, y = q.popleft()

            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n:
                    if dest[nx][ny] > dest[x][y]+1:
                        dest[nx][ny] = dest[x][y]+1
                        q.append((nx, ny))

        return dest

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #DP풀이
        #top-left 로 좌표가 1일때 DP실행, 이후 bottom-right 실행하면서 더 작은 값으로 갱신
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


### brute-force 시간초과
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        m, n = len(mat), len(mat[0])
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]

        def bfs(x, y, d):

            visited.add((i, j))
            q.append((i, j, d))

            while q:
                x, y, d = q.popleft()
                if mat[x][y] == 0:
                    return d
                visited.add((x, y))
                for dx, dy in dirs:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < m and 0 <= ny < n and (nx,ny) not in visited:
                        q.append((nx, ny, d+1))

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    visited, q = set(), collections.deque()
                    mat[i][j] = bfs(i, j, 0)

        return mat
