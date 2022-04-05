board = [[0] * 4 for _ in range (4)]

# 이게 3분컷으로 안되면 이것만 연습해야한다.
# 아무런 고민이 없어야...
n = 4
q = [(1, 1)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(4):
    while q:
        x, y = q.pop(0)

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if board[nx][ny] == 0 and 0 < nx < n and 0 < ny < n:
                x = nx, y = ny
                board[x, y] += 1

print(board)



