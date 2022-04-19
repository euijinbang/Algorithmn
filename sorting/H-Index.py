"""
어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고
나머지 논문이 h번 이하 인용되었다면 h의 최댓값

n-i = citations[i]에 해당하는 수 이상만큼 인용한 논문의 개수
"""

def solution(citations):
    citations.sort()
    answer = 0
    n = len(citations)

    for i in range(n):
        hIndex = n - i
        if citations[i] >= hIndex:
            answer = hIndex
            break

    return answer


print(solution([3, 0, 6, 1, 5]))

