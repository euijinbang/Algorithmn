N = 3
board = [
    [1, 1, 10],
    [1, 5, 1],
    [2, 2, -1]
]

visited = [[0] * 3 for _ in range(3)]

# N = int(input())
# board = []
# for _ in range(N):
#     board.append(list(map(int, input().split())))
#
# visited = [[0] * N for _ in range(N)]


def dfs(x, y):
    global flag
    if x < 0 or x >= N or y < 0 or y >= N:
        return

    if board[x][y] == -1:
        flag = True

    if visited[x][y] == 0:
        visited[x][y] = 1
        dfs(x + board[x][y], y)
        dfs(x, y + board[x][y])


flag = False
dfs(0, 0)

if flag == True:
    result = "HaruHaru"
else:
    result = "Hing"

print(result)