from itertools import combinations


def backtrack(n, tmp):
    global result

    if n == N:
        flag = True
        # 임의의 두 수의 합이 9라면 리턴
        x = list(combinations(tmp, 2))
        for k in x:
            if sum(k) == 9:
                flag = False
        if flag:
            result.append(tmp.copy())
        return

    for i in range(1, 10):
        tmp.append(i)
        backtrack(n+1, tmp)
        tmp.pop()


N = 10000
result = []
backtrack(0, [])

print(len(result))
