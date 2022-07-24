from collections import defaultdict
import bisect


def binarySearchLeft(scores, q_score):
    """
    scores 정렬된 리스트 안에
    q_score 가 있으면 가장 왼쪽의 index를 반환
    없으면

    100 150 150 150 150 200 300
    100 -> 0
    150 -> 1
    170 -> 5
    """

    left, right = 0, len(scores)
    while left < right:
        mid = (left + right) // 2
        if q_score <= scores[mid]:
            right = mid
        else:
            left = mid + 1  # lower_bound
    return left


def solution(info, query):
    answer = []
    infos = defaultdict(list)

    for data in info:
        items = data.split()
        conditions, score = tuple(items[:4]), int(items[-1])
        infos[conditions].append(score)

    for q in query:
        qs = q.split()
        q = list(filter(lambda x: x != 'and', qs))
        q_conditions, q_score = q[:-1], int(q[-1])

        # 조건을 필터링한다.
        conditions_list = list(infos.keys())
        for q_condition in q_conditions:  # 쿼리 조건을 순회하면서 리스트 재할당(재구성)
            if q_condition == "-":
                continue
            conditions_list = list(filter(lambda x: q_condition in x, conditions_list))

        # 조건에 부합하는 리스트만 남는다. == conditions_list
        # 조건에 부합하는 리스트의 점수 리스트를 가져와서, 이분탐색한다.

        # 이분탐색 위해 오름차순 정렬
        q_infos = [sorted(infos[x]) for x in conditions_list]
        q_result = 0

        for scores in q_infos:
            idx = binarySearchLeft(scores, q_score)
            # idx = bisect.bisect_left(scores, q_score)
            cnt = len(scores) - idx     # 해당 점수 이상인 점수의 갯수
            q_result += cnt

        answer.append(q_result)

    return answer


if __name__ == '__main__':
    ans = solution(
        ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
         "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
        ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
         "- and - and - and - 150"])

    print(ans)