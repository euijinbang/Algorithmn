def solution(participant, completion):
    """
    동명이인 체크하기 위해 partTable의 key를 name, val 을 인원수로 설정
    참가자 테이블에서 완주 선수들 수를 빼고
    최종 결과가 1명이상 남으면 그 선수를 반환
    """

    partTable = {}  # name : num

    for p in participant:
        if p in partTable:
            partTable[p] += 1
        else:
            partTable[p] = 1

    for c in completion:
        if c in partTable:
            partTable[c] -= 1

    for key, val in partTable.items():
        if val > 0:
            return key

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))