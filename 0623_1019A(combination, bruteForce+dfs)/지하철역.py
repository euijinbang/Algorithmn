N = 10
stations = [120, 200, 40, 30, 70, 280, 50, 170, 130, 80]
combs = []

result = 0
def combination(cnt, start, comb):
    global result

    """
    1. 오름차순으로 조합 선택
    2. 인접여부 검사
    3. 인접여부 통과시 2가지 경우에 대해 각각 최댓값 갱신
    """
    if cnt == 4:
        # 인접여부 검사
        for k in range(3):
            if (comb[k+1] - comb[k]) <= 1:
                return

        if (comb[3] + N - comb[0]) <= 1:
            return

        # 통과시 각각 최댓값 갱신
        s1 = (stations[comb[0]] + stations[comb[1]]) ** 2 + (stations[comb[2]] + stations[comb[3]]) ** 2
        s2 = (stations[comb[0]] + stations[comb[3]]) ** 2 + (stations[comb[1]] + stations[comb[2]]) ** 2
        result = max(result, s1, s2)
        return

    for i in range(start, N):
        comb.append(i)
        combination(cnt+1, i+1, comb)
        comb.pop()


combination(0, 0, [])

print(result)



