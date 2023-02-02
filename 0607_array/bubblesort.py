def bubbleSort(arr, n):
    for i in range(1, n):
        for j in range(0, n-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


print(bubbleSort([3, 2, 1], 3))

