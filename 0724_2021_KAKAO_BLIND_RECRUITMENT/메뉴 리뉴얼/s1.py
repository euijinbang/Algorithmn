from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    answer = []
    d = defaultdict(int)

    # 갯수 2개부터 모든 조합별 counter를 만든다.
    for order in orders:
        order = sorted(order)
        for i in range(2, len(order)+1):
            menus = combinations(order, i)
            for menu in menus:
                d[''.join(menu)] += 1

    d2 = defaultdict(set)  # key:val = 메뉴갯수: (코스, 주문수)

    # 구하고자 하는 코스 수 별로 (코스, 주문수) 리스트를 만든다.
    for cnt in course:
        for key, val in d.items():
            if val >= 2 and len(key) == cnt:
                d2[len(key)].add((key, val))

    # (코스, 주문수) 를 정렬해서 가장 많이 주문된 코스를 뽑는다.
    for key, list_val in d2.items():
        max_order_cnt = 2

        for c, order_cnt in list_val:
            if order_cnt >= max_order_cnt:
                max_order_cnt = order_cnt

        for c, order_cnt in list_val:
            if order_cnt == max_order_cnt:
                answer.append(c)
                print(max_order_cnt, c)


    answer.sort()
    return answer