"""
역의 갯수와 각 역의 사용자 수가 주어진다.
두 개의 노선을 추가로 개설할 때 두 노선의 타당도의 합의 최댓값을 구하라.

타당도 = (역 1의 사용자 수 + 역 2의 사용자 수 )^2

조건
1. 노선의 출발지와 도착지는 인접할 수 없다.
2. 하나의 노선의 출발지와 도착지는 서로 다른 노선의 출발지나 도착지와 인접할 수 없다.
3. 두 노선은 서로 겹칠 수 없다.
"""
import itertools
import math

N = 10
users = [120, 200, 40, 30, 70, 280, 50, 170, 130, 80]


def calcValue(i, j):
    return math.pow(users[i] + users[j], 2)


# 오름차순 정렬
total_stations = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
stations = []
max_num = 0
for combination in itertools.combinations(total_stations, 4):
    stations = combination
    flag = True

    # 인접 여부 확인
    for i in range(3):
        if stations[i + 1] - stations[i] <= 1:
            flag = False
    if stations[0] + N - stations[3] <= 1:
        flag = False

    # 타당도 계산
    if flag:
        valid1 = calcValue(stations[0], stations[1]) + calcValue(stations[2], stations[3])
        valid2 = calcValue(stations[1], stations[2]) + calcValue(stations[3], stations[0])
        max_num = max(max_num, int(valid1))
        max_num = max(max_num, int(valid2))

print(max_num)







