T = int(input())
for tc in range(1, T+1):
    # n : 전체 삼각형 높이
    # k : 작은 삼각형 블럭개수
    n, k = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]

    # 삼각형 높이
    h = int((k*2)**0.5)

    result = 0
    for i in range(n-h+1):
        for j in range(i+1):
            # 꼭짓점 탐색
            # print('top:', mat[i][j])
            tmp = mat[i][j]

            # 작은 삼각형 내부의 숫자 합산
            t = 1
            while t < h:
                # print(mat[i + t][j:j + t + 1])
                for l in range(j, j+t+1):
                    tmp += mat[i+t][l]
                ### or ###
                # tmp += sum(mat[i + t][j:j + t + 1])
                t += 1
            # print('tmp:', tmp)
            # print('result:', result)

            if tmp > result:
                result = tmp

    print('#{} {}'.format(tc, result))