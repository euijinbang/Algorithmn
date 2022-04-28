from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        start = (sr, sc)

        n, m = len(image), len(image[0]) # 행, 열
        visited = [[False] * m for _ in range(n)]
        startColor = image[sr][sc]

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        q = deque()
        q.append(start)
        visited[sr][sc] = True
        image[sr][sc] = newColor

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    if image[nx][ny] == startColor:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        image[nx][ny] = newColor

        return image