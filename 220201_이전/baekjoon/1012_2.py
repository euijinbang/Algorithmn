import sys
sys.stdin = open("1012.txt")

# 이차원배열의 정점을 돌면서 dfs 실행한다. 방문했으면 건너뛴다. dfs 실행횟수만 계산하면된다. 재귀 제한 풀어주어야한다.
import sys
sys.setrecursionlimit(100000)

# 이하코드 사용시 i,j 덮어씌워져서 오류
# def dfs(i, j):
#     visited[i][j] = 1
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
#     for dx, dy in directions:
#         i, j = i + dx, j + dy
#         if i < 0 or i >= n or j < 0 or j >= m:  # 미해당시 다시 반복문 실행
#             continue
#         if board[i][j] == 1 and not visited[i][j]:
#             dfs(i, j)

def dfs(x, y):
    visited[x][y] = 1
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:  # 미해당시 다시 반복문 실행
            continue
        if board[nx][ny] and not visited[nx][ny]:  # 배추가 있고 방문하지 않은 경우
            dfs(nx, ny)

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    visited = [[0] * m for _ in range(n)]
    board = [[0] * m for _ in range(n)]    # 가로 m, 세로 n인 배추밭(n행 m열)
    for i in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1     # 행렬과 x,y 좌표 반대이므로 주의!

    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] and not visited[i][j]:  # 배추가 있고 방문하지 않은 경우
                dfs(i, j)
                cnt += 1

    print(cnt)