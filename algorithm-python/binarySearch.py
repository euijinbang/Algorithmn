"""
binary search 1 - 기본개념 - 리스트를 잘라서 활용 (시간초과남)
1. 리스트를 sort 한다.
2. 함수를 실행한다.
    1. 리스트의 길이가 1인데 찾는 값과 다르면 False를 리턴, 같으면 True를 리턴한다.
    2. 중간값을 찾는 데이터와 비교한다.
        - 같다면 true 를 리턴한다.
        - 다르다면
            - 중간값이 찾는 데이터보다 크면 리스트 재조정 후 함수를 호출한다.
            - 중간값이 찾는 데이터보다 작으면 리스트 재조정 후 함수를 호출한다.
"""


def binary_search(sorted_data_list, data_to_find):
    print(sorted_data_list)
    # 재귀 종료 기준
    if len(sorted_data_list) == 1:
        if sorted_data_list[0] != data_to_find:
            return False
        return True

    if len(sorted_data_list) == 0:
        return False

    mid_idx = len(sorted_data_list) // 2
    mid = sorted_data_list[mid_idx]
    print(mid)

    if mid == data_to_find:
        return True
    else:
        if mid > data_to_find:
            left = sorted_data_list[:mid_idx]
            return binary_search(left, data_to_find)
        if mid < data_to_find:
            right = sorted_data_list[mid_idx:]
            return binary_search(right, data_to_find)


sorted_data_list = sorted([4, 1, 5, 2, 3, 7])
print(binary_search(sorted_data_list, 6))

