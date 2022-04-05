import sys
sys.stdin = open("14195_input.txt")

T = int(input())


def dfs():

    pass


for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 토양 샘플의 크기
    board = []
    for i in range(N):
        board.append(list(input()))

    visited = [[0] * M for _ in range(N)]
    # 상하좌우 보는데 내가 다 방문한 곳이고, 같은 알파벳이 없으면 종료
    # A 또는 B일 때만 시작
    




    print(visited)
    print(board)
    # print("#{} {}".format(tc, answer))