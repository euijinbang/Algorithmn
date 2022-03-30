arr = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


def dfs(count):
    if count == 3:  # 3개 좌표를 택하는 경우의 수
        print('---------')
        for row in arr:
            print(row)
        return

    for i in range(3):
        for j in range(3):
            if arr[i][j] == 0:
                arr[i][j] = 1
                count += 1
                dfs(count)
                arr[i][j] = 0
                count -= 1


dfs(0)
