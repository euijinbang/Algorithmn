def solution(n, clockwise):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    arr = [[0] * n for _ in range(n)]
    x, y = 0, 0
    direction = 0
    print(arr)

    for num in range(1, n*n + 1):
        arr[x][y] = num

        x += dx[direction]
        y += dy[direction]

        if x < 0 or y < 0 or x >= n or y >= n or arr[x][y]:
            x -= dx[direction]
            y -= dy[direction]

            direction = (direction + 1) % 4
            x += dx[direction]
            y += dy[direction]

    answer = []
    for i in arr:
        answer.append(i)
        print(*i, ' ')

    print(answer)
    return answer

solution(5, 1)