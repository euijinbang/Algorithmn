"""
quick sort
- 리스트 갯수가 1개 이하면 해당 리스트를 리턴한다.
- 리스트 갯수가 1개가 아니면 리스트 맨 앞 데이터를 Pivot으로 둔다.
- left, right 리스트 변수를 만들고
- 맨 앞 데이터를 뺀 나머지 데이터를 기준점과 비교해서
    - 기준점보다 작으면 left.append
    - 기준점보다 크면 right.append
- return quicksort(left) + [pivot] + quicksort(right) 로 재귀호출한다.
"""
import random


def quickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    """
    left, right = [], []
    
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        if arr[i] > pivot:
            right.append(arr[i])
    """

    # list comprehension 적용시
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x > pivot]

    return quickSort(left) + [pivot] + quickSort(right)


data_list = random.sample(range(100), 10)
print(quickSort(data_list))
