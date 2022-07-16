def solution(N, stages):

    # 각 스테이지별 도착인원수 {1: 1, 2: 3, 3: 2, 4: 1, 5: 0, 6: 1}
    arrival_counter = dict()

    for i in range(1, N+2):
        arrival_counter[i] = 0

    for idx, stage in enumerate(stages):
        arrival_counter[stage] += 1

        # 스테이지별 실패율 저장할 배열
    f_rate = [x for x in range(N+1)]

    # 실패율 계산
    M = len(stages) # 인원수
    for stage, num in arrival_counter.items():

        # 최종 스테이지까지 클리어한 경우
        if stage >= N+1:
            continue

        # 스테이지에 도달한 유저가 없는 경우 실패율 = 0
        if M == 0:
            f_rate[stage] = 0
            continue

        fail_M = num
        fail_rate = fail_M / M

        f_rate[stage] = fail_rate
        M -= fail_M


    # 인덱스 튜플로 만든 후 실패율 높은 순, 인덱스 낮은순으로 정렬
    result = sorted([(val, idx) for idx, val in enumerate(f_rate)], key=lambda x: (-x[0], x[1]))

    ans = []
    for val, idx in result:
        if not idx: continue
        ans.append(idx)

    return ans