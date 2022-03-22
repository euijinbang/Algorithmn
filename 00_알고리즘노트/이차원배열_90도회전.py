n = 3
arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]


def rotate_90_degree(arr):
    n = len(arr) #행 길이
    m = len(arr[0]) #열 길이
    r_arr = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            r_arr[j][n-1-i] = arr[i][j]
    return r_arr


ro_90_arr = rotate_90_degree(arr)
for row in ro_90_arr:
    print(row)

