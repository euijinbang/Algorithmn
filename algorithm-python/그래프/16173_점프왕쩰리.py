N = 3
board = [
    [1, 1, 10],
    [1, 5, 1],
    [2, 2, -1]
]

visited = [[0] * 3 for _ in range(3)]
"""
dfs로 모든 경로를 탐색한다.
우, 하 방향으로 해당 칸 수만큼 이동하며 탐색한다.
"""
# N = int(input())
# board = []
# for _ in range(N):
#     board.append(list(map(int, input().split())))

visited = [[0] * N for _ in range(N)]


def dfs(x, y):
    global flag
    if x < 0 or x >= N or y < 0 or y >= N:
        return

    if board[x][y] == -1:
        flag = True

    if not visited[x][y]:
        visited[x][y] = 1
        dfs(x + board[x][y], y)
        dfs(x, y + board[x][y])


flag = False
dfs(0, 0)

if flag:
    result = "HaruHaru"
else:
    result = "Hing"

print(result)