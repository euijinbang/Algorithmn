"""
Bubble Sort is the simplest sorting algorithm
that works by repeatedly swapping the adjacent elements if they are in wrong order.
...
point > Last i element are already in place after a traverse.
...
Now, the array is already sorted, but our algorithm does not know if it is completed.
The algorithm needs one whole pass without any swap to know it is sorted.
"""


def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):

        # Last i elements are already in place
        for j in range(n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is grater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i]),
