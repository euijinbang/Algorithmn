from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        #방법1. 정석대로 풀기
        m, n = len(image), len(image[0])
        start = (sr, sc)
        q = deque([start])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        visited = [[False] * n for _ in range(m)]
        toFind = image[sr][sc]
        image[sr][sc] = newColor
        visited[sr][sc] = True

        while q:
            r, c = q.popleft()
            for d in range(4):
                nr, nc = r + dx[d], c + dy[d]
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    if image[nr][nc] == toFind:
                        image[nr][nc] = newColor
                        visited[nr][nc] = True
                        q.append((nr, nc))

        return image



        #방법2. 중복 줄이고 visited 를 사용하지 않고 풀기 => if old != newColor: 처리 필요
        old, m, n = image[sr][sc], len(image), len(image[0])
        q = deque([(sr, sc)])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        image[sr][sc] = newColor

        if old != newColor:
            while q:
                r, c = q.popleft()
                for d in range(4):
                    nr, nc = r + dx[d], c + dy[d]
                    if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == old:
                        image[nr][nc] = newColor
                        q.append((nr, nc))

        return image