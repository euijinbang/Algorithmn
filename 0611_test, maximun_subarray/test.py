from itertools import combinations
from collections import defaultdict

def solution(cards):
    n = len(cards)
    people = [x+1 for x in range(n)]
    q = list(combinations(people, 2))

    d = defaultdict(list)
    for i, v in enumerate(cards):
        for j in range(3):
            d[i+1].append([j, v[j]])

    done = set()

    # 1. 모든 조합 돌면서 done 에 있는지 확인
    # 2. 교환 원하는 카드 확인
    # 3. 교환 원하는 카드가 동일하면 패스
    # 4. 교환 후 조건을 하나라도 만족하지 않으면 패스
    # 5. 교환 진행 후 set 에 추가
    for combi in q:
        if combi[0] in done or combi[1] in done:
            continue
        a, b = combi[0], combi[1]
        want_a, want_b = min(d[a], key = lambda x: x[1]), min(d[b], key = lambda x: x[1])

        # 바꾸고자 하는 컬러 want_a[0] == want_b[0]
        if want_a[0] == want_b[0]:
            continue

        # 바꾸고자 했던 컬러의 점수
        tmp_a, tmp_b = want_a[1], want_b[1]

        # 기존 최솟값 want_a[1], want_b[1]
        # 교환
        d[a][want_a[0]][1] += 1
        d[a][want_b[0]][1] -= 1
        d[b][want_b[0]][1] += 1
        d[b][want_a[0]][1] -= 1

        if min(d[a], key = lambda x: x[1])[1] > tmp_a and min(d[b], key = lambda x: x[1])[1] > tmp_b:
            done.add(a)
            done.add(b)

        else:
            d[a][want_a[0]][1] -= 1
            d[a][want_b[0]][1] += 1
            d[b][want_b[0]][1] -= 1
            d[b][want_a[0]][1] += 1

    result = 0
    for val in d.values():
        tmp = [x[1] for x in val]
        result += min(tmp)

    return result

