from collections import deque
import sys
sys.stdin = open("minco.txt")


def set_number():
    cnt = 1  # 노드별 번호 붇이기
    for y in range(N):
        for x in range(M):
            if MAP[y][x] == 'A' or MAP[y][x] == 'S':
                num[y][x] = cnt
                cnt += 1

# def Kruskal():
#     global parent
#     global edge_lst
#     parent = [0 for _ in range(110)]
#     # init parent
#     for i in range(105):
#         parent[i] = i
#
#     edge_lst.sort(key=lambda x:x[2])
#
#     ans = 0
#     for i in range(len(edge_lst)):
#         a = edge_lst[i][0]
#         b = edge_lst[i][1]
#         if getFind(a) != getFind(b):
#             setUnion(a, b)
#             ans += edge_lst[i][2]
#     return ans


def bfs(sy, sx):
    qu = deque()
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    visited = [[0 for x in range(M)] for y in range(N)]
    visited[sy][sx] = 1
    qu.append((sy, sx, 0))

    while qu:
        now_y, now_x, now_level = qu.popleft()
        if num[now_y][now_x] > 0 and not (now_y == sy and now_x == sx):
            edge_lst.append((num[sy][sx], num[now_y][now_x], now_level))
        for t in range(4):
            ny = now_y + dy[t]
            nx = now_x + dx[t]
            if MAP[ny][nx] == '#': continue
            if visited[ny][nx] == 1: continue
            visited[ny][nx] = 1


T = int(input())

for tc in range(1, T+1):
    M, N = map(int, input().split())
    MAP = [list(input()) for _ in range(N)]
    # N x M 배열 초기화
    num = [[0 for x in range(M)] for y in range(N)]

    # 노드를 번호화
    set_number()
    # 한 노드에서 다른 노드로 가는데 걸리는 비용
    edge_lst = []
    for y in range(N):
        for x in range(M):
            if num[y][x] > 0:
                bfs(y, x)

    print(MAP)
    print(num)

    # print(Kruskal())