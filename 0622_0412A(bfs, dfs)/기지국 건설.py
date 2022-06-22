w, h = 5, 3
# cells = [
#     [300, 410, 150, 55, 370],
#     [120, 185, 440, 190, 450],
#     [165, 70, 95, 420, 50]
# ]
# 300 410 150 55 370
# 120 185 440 190 450
# 165 70 95 420 50

cells = []
for row in range(h):
    cells.append(list(map(int, input().split())))

visited = set()
ed = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 0), (0, -1)]
od = [(-1, 0), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]


def dfs(cnt, sum, i, j):
    global res
    if cnt == 4:
        if sum > res:
            res = sum
        return

    # 홀수열과 짝수열 분리하여 dfs 진행
    if j % 2 == 0:
        for di, dj in ed:
            ni, nj = i + di, j + dj
            if ni < 0 or ni >= h or nj < 0 or nj >= w:
                continue
            if (ni, nj) in visited:
                continue
            visited.add((ni, nj))
            dfs(cnt + 1, sum + cells[ni][nj], ni, nj)
            visited.remove((ni, nj))
    else:
        for di, dj in od:
            ni, nj = i + di, j + dj
            if ni < 0 or ni >= h or nj < 0 or nj >= w:
                continue
            if (ni, nj) in visited:
                continue

            visited.add((ni, nj))
            dfs(cnt + 1, sum + cells[ni][nj], ni, nj)
            visited.remove((ni, nj))


def findAdj(sum, i, j):
    global res
    adj = []
    if j % 2 == 0:
        for di, dj in ed:
            ni, nj = i + di, j + dj
            if ni < 0 or ni >= h or nj < 0 or nj >= w:
                continue
            adj.append(cells[ni][nj])

    else:
        for di, dj in od:
            ni, nj = i + di, j + dj
            if ni < 0 or ni >= h or nj < 0 or nj >= w:
                continue
            adj.append(cells[ni][nj])

    # 3개 이상인 경우만 계산
    if len(adj) >= 3:
        adj.sort(reverse=True)
        print(adj)
        for k in range(3):
            sum += adj[k]

    if sum > res:
        res = sum


res = 0
for r in range(h):
    for c in range(w):
        print(r, c)
        # 1. dfs 로 4개 선택
        visited.add((r, c))
        dfs(1, cells[r][c], r, c)
        visited.remove((r, c))

        # 2. 정점 중심으로 큰 값 3개 선택
        findAdj(cells[r][c], r, c)


print(res * res)
