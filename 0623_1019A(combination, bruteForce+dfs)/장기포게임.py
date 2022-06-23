"""
sol1
1. 4방탐색
    2. while 반복문으로 알을 만날 때 까지 같은 방향으로 이동
    3. 알을 만나면 바로 뒤 좌표 설정
    4. 범위 내에서 반복
        뒤 좌표가 알이면 알 잡고, dfs, 빠져나오면 반복문 break
        뒤 좌표가 알이 아니면 dfs
            while ... 같은 방향으로 계속 이동

sol2
1. 4방탐색
    2. 알을 처음 만났는지 여부 세팅
    3. while 반복문으로 같은 방향으로 좌표를 계속 이동, 범위체크
        - 아직 알을 만나지 않았다면 알을 만날때 까지 반복.
        - 알을 이전에 만났는데, 현 위치가 알이면, dfs 진행
            빠져나오고 위치가 알이라면 알을 잡는다.

"""

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
n = 8
cells = [[0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 1, 0, 0, 1, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 2, 0, 0, 0, 0, 0],
         [1, 0, 0, 1, 0, 0, 1, 0]]

catch = set()
def dfs(cnt, r, c):
    if cnt == 3:
        return
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]

        # 다음 좌표가 범위 내고 0이라면 계속 이동
        while 0 <= nr < n and 0 <= nc < n and not cells[nr][nc]:
            nr += dr[d]
            nc += dc[d]

        # 1 발견하면 한 칸 더 이동
        nr += dr[d]
        nc += dc[d]

        # 범위 내에서 좌표 이동하며(같은 방향) 반복
        while 0 <= nr < n and 0 <= nc < n:
            if cells[nr][nc]:  # 알 발견시 잡고 판 변경 및 복구
                cells[nr][nc] = 0
                catch.add((nr, nc))
                dfs(cnt+1, nr, nc)
                cells[nr][nc] = 1
                break
            else:   # 알 미발견시 dfs 진행
                dfs(cnt+1, nr, nc)

            nr += dr[d]
            nc += dc[d]


for i in range(n):
    for j in range(n):
        if cells[i][j] == 2:    # 시작점 저장 및 0으로 변경
            sx, sy = i, j
            cells[i][j] = 0

dfs(0, sx, sy)

print(len(catch))
