"""
The selection sort algorithm sorts an array by
repeatedly finding the minimum element(considering ascending order)
from unsorted part and putting it at the beginning.
"""


def selectionSort(arr):

    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


arr = [12, 11, 13, 5, 6]

selectionSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i])
