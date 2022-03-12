"""
그리디 알고리즘
1. sugar_list 를 큰 수부터 확인
2. 5의 배수이면 스탑, 5의 배수가 아니면 3씩 줄여나간다.
3. 설탕이 남아있으면 -1을 반환.
"""


def min_sugar_bags(suger_bag_list, sugar_weight):

    suger_bag_list.sort(reverse=True)
    total_bag_count = 0

    while sugar_weight > 0:
        if sugar_weight % 5 == 0:
            cnt = sugar_weight // 5
            total_bag_count += cnt
            sugar_weight -= cnt * 5
            break

        sugar_weight -= 3
        total_bag_count += 1

    if sugar_weight:
        return -1

    else:
        return total_bag_count


k = int(input())

print(min_sugar_bags([3, 5], k))
