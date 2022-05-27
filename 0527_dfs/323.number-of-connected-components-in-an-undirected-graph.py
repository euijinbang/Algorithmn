"""
amazon

1. graph build
2. 해당노드 미방문시 dfs 시작
3. 시작시마다 cnt + 1

edges[i] = [ai, bi] means there is an edge between ai and bi in graph
edges = [[0, 1], [1, 2], [3, 4]]
"""

# 1. edge case 처리
# 2. 양방향 그래프 만들기
# 3. visited, 갯수 세팅
# 4. dfs 함수 - 노드의 인접노드 돌면서 미방문시 방문추가, dfs
# 5. 그래프의 노드 미방문시 방문 추가, 갯수추가, dfs 실행
# 6. 갯수 반환
import collections

n = 3   # number of nodes
edges = [[0, 1], [1, 2], [3, 4]]

if n == 1:
    print(0)

graph = collections.defaultdict(list)
for node1, node2 in edges:
    graph[node1].append(node2)
    graph[node2].append(node1)

visited = set()
components = 0

def dfs(node):
    for adj in graph[node]:
        if adj not in visited:
            visited.add(adj)
            dfs(adj)

for node in graph:
    if node in visited:
        continue
    else:
        visited.add(node)
        components += 1
        dfs(node)

print(components)



