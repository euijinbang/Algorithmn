"""
이동시 좌표 넘어가는 부분은 모두 0으로 처리
"""
n = 3
arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in arr:
    print(row)
print('---------')

def mv_right(arr):
    mv_arr = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n-1):
            mv_arr[i][j+1] = arr[i][j]
    return mv_arr


mv_right_arr = mv_right(arr)
for row in mv_right_arr:
    print(row)
print('---------')


def mv_down(arr):
    mv_arr = [[0]*n for _ in range(n)]
    for i in range(n-1):
        for j in range(n):
            mv_arr[i+1][j] = arr[i][j]
    return mv_arr


mv_down_arr = mv_down(arr)
for row in mv_down_arr:
    print(row)
print('---------')



def mv_left(arr):
    mv_arr = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(1, n):
            mv_arr[i][j-1] = arr[i][j]
    return mv_arr


mv_left_arr = mv_left(arr)
for row in mv_left_arr:
    print(row)
print('---------')



def mv_up(arr):
    mv_arr = [[0]*n for _ in range(n)]
    for i in range(1, n):
        for j in range(n):
            mv_arr[i-1][j] = arr[i][j]
    return mv_arr


mv_up_arr = mv_up(arr)
for row in mv_up_arr:
    print(row)
print('---------')


