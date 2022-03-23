# 특정 위치까지 이동하는 최단시간을 구하는 문제
import sys
sys.stdin = open("1697.txt")


from collections import deque

MAX = 100001
n, k = map(int, input().split())
visited = [0] * MAX

def bfs():
    q = deque([n])
    while q:
        now_pos = q.popleft()

        if now_pos == k:
            # print(visited)
            return visited[now_pos]

        for next_pos in (now_pos - 1, now_pos + 1, now_pos * 2):
            if 0 <= next_pos < MAX and visited[next_pos] == 0:
                q.append(next_pos)
                visited[next_pos] = visited[now_pos] + 1

print(bfs())



