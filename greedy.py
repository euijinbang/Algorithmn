"""
매 순간 최적이라고 생각되는 경우를 선택
"""

"""
1. 동전 문제
최소한의 동전을 사용하여 거스름돈을 거슬러준다.
"""


def min_coin_count(value, coin_list):
    total_coin_count = 0
    details = []
    coin_list.sort(reverse=True)  # 큰 동전 부터 정렬

    for coin in coin_list:
        coin_num = value // coin
        total_coin_count += coin_num
        details.append([coin, coin_num])
        value = value - (coin_num * coin)

    return total_coin_count, details


print(min_coin_count(4720, [10, 100, 50, 500]))
# (13, [[500, 9], [100, 2], [50, 0], [10, 2]])


"""
2. 부분 배낭 문제 (Fractional knapsack Problem)
무게 제한이 k인 배낭에 최대 가치를 가지도록 물건을 넣는다.
각 물건은 무게(w)와 가치(v)를 가진다.
단, 물건은 쪼갤 수 있다.
"""


def get_max_value(data_list, capacity):
    # 무게 대비 가치가 높은 순으로 정렬
    data_list = sorted(data_list, key=lambda x:x[1]/x[0], reverse=True)

    total_value = 0
    details = []

    for data in data_list:
        if capacity - data[0] >= 0:
            capacity -= data[0]
            total_value += data[1]
            details.append([data[0], data[1], 1])  # 무게, 가치, 1이면 전체를 다 넣었다.
        else:  # 물건의 일부만 넣어야 함
            fraction = capacity / data[0]  # 0.6개
            capacity -= data[0] * fraction
            total_value += data[1] * fraction
            details.append([data[0], data[1], fraction])
            break  # 다음 물건을 볼 필요가 없으니 멈춘다

    return total_value, details


# 물건 튜플로 표현 : 물건 5개 (무게, 가치)
data_list_g = [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]

print(get_max_value(data_list_g, 30))
# (24.5, [[10, 10, 1], [15, 12, 1], [20, 10, 0.25]])

