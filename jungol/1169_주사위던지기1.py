# N = 3
# 주사위 던진 횟수 == 깊이

K = 3


def sol1(start, comb):
    """
    매 깊이 들어갈 때 마다 다시 스타트(1)부터 시작
    모두 중복된다
    중복순열
    """
    if len(comb) == K:
        print(comb)
        return

    for i in range(start, 7):
        comb.append(i)
        sol1(start, comb)
        comb.pop()

sol1(1, [])


print('-------------')


def sol2(start, comb):
    """
    매 깊이 들어갈 때 마다 그 전 선택한 수부터 시작
    중복을 제외한다
    중복조합
    """
    if len(comb) == K:
        print(comb)
        return

    for i in range(start, 7):
        comb.append(i)
        sol2(i, comb)
        comb.pop()

sol2(1, [])



print('-------------')


def sol3(start, comb):
    """
    중복되는 숫자가 없다
    순열
    """
    if len(comb) == K:
        print(comb)
        return

    for i in range(start, 7):
        comb.append(i)
        sol3(i+1, comb)
        comb.pop()

sol3(1, [])

