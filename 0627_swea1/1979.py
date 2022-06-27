"""
1979. 어디에 단어가 들어갈 수 있을까
1. 가로세로 검사 각각 진행
2. cnt 세다가 벽 만나면 K 검사
3. 끝까지 가서야 완성된 경우 K 검사
"""

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    cells = [list(map(int, input().split())) for _ in range(N)]

    # 띠를 두른 경우
    # cells = [list(map(int, input().split())) + [0] for _ in range(N)]
    # cells.append([0]*(N+1))

    ans = 0
    for i in range(N):
        # 행을 검사
        cnt_r = 0
        for j in range(N):
            if cells[i][j] == 1:    # 흰색 부분 발견
                cnt_r += 1
            else:
                # 벽이라면
                if cnt_r == K:
                    ans += 1
                cnt_r = 0

        # 끝까지 가서야 완성된 경우
        if cnt_r == K:
            ans += 1

        # 열을 검사
        cnt_c = 0
        for j in range(N):
            if cells[j][i] == 1:
                cnt_c += 1
            else:
                if cnt_c == K:
                    ans += 1
                cnt_c = 0

        if cnt_c == K:
            ans += 1

    print("#{} {}".format(tc, ans))
