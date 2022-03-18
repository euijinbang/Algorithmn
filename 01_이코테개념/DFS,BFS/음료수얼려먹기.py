N, M = 4, 5
graph = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]


def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:  # 범위를 벗어난 경우 종료
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1

        dfs(x, y-1)     # 상하좌우 검사
        dfs(x, y+1)
        dfs(x-1, y)
        dfs(x+1, y)
        return True
    return False  # 이미 방문한 경우 종료

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:       # 각 노드의 x, y 좌표를 파라미터로 확인
            result += 1

print(result)
