from collections import deque

n = 5
board = [[1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 2]]

visited = [[False] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

starts = [(0, 0), (4, 4)]

count_a = 1
count_b = 1


def bfs(board, visited, starts, count_a, count_b):
    q = deque()
    for start in starts:
        q.append(start)
        visited[start[0]][start[1]] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                q.append((nx, ny))
                if board[x][y] == 1:
                    board[nx][ny] = 1
                    count_a += 1
                if board[x][y] == 2:
                    board[nx][ny] = 2
                    count_b += 1

                visited[nx][ny] = True

    return board, count_a, count_b


result = bfs(board, visited, starts, count_a, count_b)
for i in range(n):
    print(result[0][i])

print("1의 갯수: {}".format(result[1]))
print("2의 갯수: {}".format(result[2]))
