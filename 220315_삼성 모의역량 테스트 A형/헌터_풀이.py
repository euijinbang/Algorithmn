def go(k, s, cnt, routes):  # k: 현재위치(candidates[k]), s: 걸린 시간, cnt: 방문수
    global min_result
    global min_routes
    if s > min_result:
        return
    if cnt == len(candidates) - 1:  # base case
        min_result = min(min_result, s)
        min_routes = routes
        return

    num, r, c = candidates[k][1:]
    # 1. 방문체크
    candidates[k][0] = 2

    # 2. 몬스터라면 같은 번호 고객을 찾아 status를 1로 변경
    if num > 0:
        for i in range(1, len(candidates)):
            if candidates[i][1] == -num:
                candidates[i][0] = 1

    # next
    for i in range(1, len(candidates)):
        nstatus, nnum, ni, nj = candidates[i]
        if nstatus == 1:
            distance = abs(r - ni) + abs(c - nj)
            go(i, s+distance, cnt + 1, routes+[nnum])

    # return 전 원상복귀
    if num > 0:
        for i in range(1, len(candidates)):
            if candidates[i][1] == -num:
                candidates[i][0] = 0
    candidates[k][0] = 1


T = int(input())
for t in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    candidates = [[1, 0, 0, 0]]  # (status, num, i, j)  # status => 0:대기, 1:준비됨, 2:방문함
    for i in range(n):
        for j in range(n):
            if matrix[i][j] > 0:  # 몬스터
                candidates.append([1, matrix[i][j], i, j])
            elif matrix[i][j] < 0:  # 고객
                candidates.append([0, matrix[i][j], i, j])

    min_result = float('inf')
    min_routes = []
    go(0, 0, 0, [])
    print(f'#{t} {min_result}')
    print(f'#{t} routes: {min_routes}')  # 경로 출력