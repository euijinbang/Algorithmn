"""
A(0,0) 에서 B, C, D, E 로 가는 각각의 최단 경로 구하기
"""
N = 5
MAX = 99999
graph = [
    [MAX, 3, MAX, 9, 5],
    [MAX, MAX, 7, MAX, 1],
    [MAX, MAX, MAX, 1, MAX],
    [MAX, MAX, MAX, MAX, MAX],
    [MAX, MAX, 1, MAX, MAX]
]

used = [False] * N

result = [MAX, 3, MAX, 9, 5]


def setVia():
    """
    result 값이 가장 작은 (미방문)경유지를 선택한다.
    """
    min_via = 999
    min_via_index = 999
    for i, v in enumerate(result):
        if not used[i]:
            if v < min_via:
                min_via = v
                min_via_index = i

    return min_via, min_via_index


def dijk(sr, sc):

    for _ in range(N-1):
        via, via_index = setVia()
        used[via_index] = True

        for i, v in enumerate(result):
            # 시작점은 유지
            if i == sr:
                continue
            # 해당 경유지인 경우 유지
            if i == via_index:
                continue

            # A에서 C로 바로 가는 경우 vs. A-B-C 중 작은 값으로 갱신
            direct = result[i]
            via_route = result[via_index] + graph[via_index][i]  # A-B, B-C
            result[i] = min(direct, via_route)

    print(result)


sx, sy = 0, 0
used[0] = True
dijk(sx, sy)

