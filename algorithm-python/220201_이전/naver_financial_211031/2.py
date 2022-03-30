n = 5
jump = 3
result = [5, 2]

board = [[0] * n for x in range(n)]
print(board)

di = [0, jump, 0, -jump]
dj = [jump, 0, -jump, 0]

k = 0
cnt = 1
i, j = 0, -jump

while cnt <= n ** 2:
    ni, nj = i + di[k], j + dj[k]
    if ni in range(n) and nj in range(n) and board[ni][nj] == 0:
        board[ni][nj] = cnt
        i, j = ni, nj
        cnt += 1
    elif ni not in range(n):
        ni = ni - dj[k]
        while True:
            ni += jump
            if ni in range(n):
                break
            else:
                jump -= 1
    elif nj not in range(n):
        nj = nj - dj[k]
        while True:
            nj += jump
            if nj in range(n):
                break
            else:
                jump -= 1
    else:
        k = (k + 1) % 4


print(board)