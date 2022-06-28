"""
5356. 세로로 말해요
<< 2차원 배열 >>

1. 이차원 배열 받으면서 max 갱신
2. 만들어둔 배열 돌면서, 해당 숫자 인덱스가 해당 행 길이보다 작으면 프린트함
-- 행 길이가 4라면 column index = 0, 1, 2, 3 까지 가능
"""

T = int(input())

for tc in range(1, T+1):
    chars = [0] * 5
    max_col = 0
    for i in range(5):      # 이차원 배열 받으면서 max도 갱신
        chars[i] = list(input())
        if len(chars[i]) > max_col:
            max_col = len(chars[i])

    print("#{}".format(tc), end=" ")

    for i in range(max_col):
        for j in range(5):
            if i < len(chars[j]):   # 열번호(i)가 길이보다 작으면 프린트
                print(chars[j][i], end="")
    print()

