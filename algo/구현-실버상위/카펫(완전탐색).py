"""
yellow 의 약수를 찾는다.
yellow_garo >= yellow_sero 인 경우
노란색 가로+2 곱하기 세로+2 = yellow + brown 인 경우 결과를 구한다.
"""
import math


def solution(brown, yellow):
    result = []
    for i in range(1, round(math.sqrt(yellow))+1):

        if yellow % i == 0:
            yellow_garo = yellow // i
            yellow_sero = i

            if yellow_garo >= yellow_sero:
                if ((yellow_sero+2) * (yellow_garo+2)) == brown + yellow:
                    result.append(yellow_garo + 2)
                    result.append(yellow_sero + 2)
                    return result

brown = 10
yellow = 2
#
# brown = 8
# yellow = 1
#
# brown = 24
# yellow = 24


print(solution(brown, yellow))
