"""
가지치기 연습
7 또는 8
1 - 9
1, 2, 7, 9
1 - 9

기본적인 가지치기는 used 를 사용하고 (순열에서 필수)
추가적인 가지치기가 필요하면 위나 아래에 추가한다.
"""

used = [False] * 10


# 위에다 하는 방법, 아래에 하는 방법이 있다.
def backtracking(start, comb):
    # 가지치기 위에다 하는 방법 (넘어간 후에 다시 돌아감)
    # if len(comb) == 1 and (comb[0] != 7 and comb[0] != 8):
    #     return
    #
    # if len(comb) == 3 and (comb[2] != 1 and comb[2] != 2 and comb[2] != 7 and comb[2] != 9):
    #     return

    if len(comb) == K:
        print(comb)
        return

    for i in range(start, 10):
        # 기본 가지치기
        if used[i] == 1: continue
        used[i] = 1
        # 가지치기 아래에다 하는 방법 (다음 레벨로 넘어가기 전에 검사)
        if len(comb) == 0 and (i != 7 and i != 9): continue
        if len(comb) == 2 and (i != 1 and i != 2 and i != 7 and i != 9): continue

        comb.append(i)
        backtracking(1, comb)
        comb.pop()
        used[i] = 0


K = 4
backtracking(1, [])
