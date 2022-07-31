from collections import Counter
from itertools import combinations_with_replacement as cwr

def solution(n, info):

    answer = []
    info = info[::-1]
    max_diff = -1

    # 0부터 10까지 n개의 수를 조합으로 만든다.
    # n = 3 이라면 (0, 0, 0), (0, 0, 1), (0, 0, 2), ...
    for c in cwr(range(0, 11), n):
        ryan, apeach = 0, 0
        tmp_ans = [0 for _ in range(11)]

        c = Counter(c)  # {0:3}, {0:2, 1:1}, ...
        for i in range(0, 11):
            if info[i] < c[i]: #라이언 승
                ryan += i
            elif info[i]:   #어피치 승
                apeach += i

            tmp_ans[i] = c[i]

        # 라이언 승리시 최대치 갱신
        if ryan > apeach:
            diff = ryan - apeach
            if max_diff < diff:
                max_diff = diff
                answer = tmp_ans

    if answer:
        return answer[::-1]
    else:
        return [max_diff]
