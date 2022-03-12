"""
binary search 2 - start, end 인덱스를 활용
1. 리스트를 sort 한다.
2. 함수를 실행한다.
    0. start 가 end 를 넘어가면 False 를 리턴한다.
    1. 중간 인덱스를 구한다.
    3. 만약 찾는 값이 중간값보다 작으면
        함수를 재호출한다. 이때, end 는 mid - 1 이다.
    4. 만약 찾는 값이 중간값보다 크면
        함수를 재호출한다. 이때, start 는 mid + 1 이다.
    5. 만약 찾는 값이 중간값과 일치하면
        True 를 리턴한다.
"""


data_list = sorted([4, 1, 5, 2, 3, 7])


def binary_search(value, start, end):
    # 재귀 종료 기준 - 일치 하는 값이 없으면 start 가 end 를 넘어감
    if start > end:
        return False

    mid = (start + end) // 2

    if data_list[mid] > value:
        return binary_search(value, start, mid - 1)
    elif data_list[mid] < value:
        return binary_search(value, mid + 1, end)
    else:
        return True


print(binary_search(4, 0, len(data_list) - 1))

