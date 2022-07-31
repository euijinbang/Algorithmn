def solution(id_list, report, k):


    # 1. 신고한 사람의 목록 딕셔너리
    reporter = dict()

    # 2. 인원별 신고당한 숫자 딕셔너리
    reported_counter = dict()

    # 3. 신고당한 사랑 목록 리스트
    reported = list()

    for name in id_list:
        reporter[name] = set()
        reported_counter[name] = 0

    # 인원별 신고한 사람의 목록 구하기
    for r in report:
        s, e = r.split(' ')
        reporter[s].add(e)

    # 1로부터 2 구하기
    for key, val in reporter.items():
        for v in list(val):
            reported_counter[v] += 1

    # 신고당한 사람의 최종목록 구하기
    for key, val in reported_counter.items():
        if val >= k:
            reported.append(key)

    # 4. 신고한사람 목록 돌면서 신고당한 사람과 일치하는 갯수 반환
    result = []
    for key, val in reporter.items():
        cnt = 0
        for rp in val:
            if rp in reported:
                cnt += 1
        result.append(cnt)

    return result