"""
2차원 배열 문제
board[i][j] = board[i-1][0] + board[i-1][1] + ... + board[i-1][j]
규칙을 찾으면 된다.
"""
T = int(input())

board = [[0] * 15 for _ in range(15)]

for i in range(14):
    board[0][i] = i+1

for i in range(1, 15):
    for j in range(15):
        for s in range(0, j+1):
            board[i][j] += board[i-1][s]

# print(board)
for tc in range(T):
    k = int(input())
    n = int(input())
    print(board[k][n-1])
