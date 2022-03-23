import sys
sys.stdin = open("1012.txt")

import sys
sys.setrecursionlimit(100000)
t = int(input())

def dfs(idx, node):
    visited[idx] = 1
    for w in adj[idx]:
        link_idx = nodes.index(w)
        if not visited[link_idx]:
            dfs(link_idx, w)


for tc in range(t):
    m, n, k = map(int, input().split())
    visited = [0]*k
    nodes = []
    adj = [[] for _ in range(k)]

    for i in range(k):
        n1, n2 = map(int, input().split())
        node = (n1, n2)
        nodes.append(node)

    for j in range(k):
        for e in range(k):
            # x축이 같고 y축이 1차이
            if nodes[j][0] == nodes[e][0]:
                if abs(nodes[j][1] - nodes[e][1]) == 1:
                    adj[j].append(nodes[e])
                    # adj[e].append(nodes[j])

            # y축이 같고 x축이 1차이
            if nodes[j][1] == nodes[e][1]:
                if abs(nodes[j][0] - nodes[e][0]) == 1:
                    adj[j].append(nodes[e])
                    # adj[e].append(nodes[j])

    cnt = 0
    for idx, node in enumerate(nodes):
        if not visited[idx]:
            dfs(idx, node)
            cnt += 1

    print (cnt)


