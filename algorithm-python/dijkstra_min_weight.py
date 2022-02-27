mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

import heapq

# 시작 정점에서 다른 정점까지의 최단거리
def dijkstra(graph, start):
    # 1. initialize distances
    distances = {node: float('inf') for node in graph}  # node 별로 value를 inf 로 초기화
    distances[start] = 0

    # 2. initialize heap-queue
    queue = []
    heapq.heappush(queue, [distances[start], start])

    # print(distances)    # {'A': 0, 'B': inf, 'C': inf, 'D': inf, 'E': inf, 'F': inf}
    # print(queue)    # [[0, 'A']]

    # 3. start logics
    # until queue exists
    while queue:
        # 3-1. pop data(with the highest priority) from heapq
        current_distance, current_node = heapq.heappop(queue)  # [0, 'A']

        # 3-2. if distances is less than current_distance : continue
        if distances[current_node] < current_distance:
            continue

        # 3-3. else, check adjs
        for adjacent, weight in graph[current_node].items():  # ('B', 8) ('C', 1) ('D', 2)
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance  # {'A': 0, 'B': 8, 'C': inf, 'D': inf, 'E': inf, 'F': inf}
                heapq.heappush(queue, [distance, adjacent])

                print(distances)
                print(queue)

    return distances


"""
distances
queue

{'A': 0, 'B': 8, 'C': inf, 'D': inf, 'E': inf, 'F': inf}
[[8, 'B']]
{'A': 0, 'B': 8, 'C': 1, 'D': inf, 'E': inf, 'F': inf}
[[1, 'C'], [8, 'B']]
{'A': 0, 'B': 8, 'C': 1, 'D': 2, 'E': inf, 'F': inf}
[[1, 'C'], [8, 'B'], [2, 'D']]
{'A': 0, 'B': 6, 'C': 1, 'D': 2, 'E': inf, 'F': inf}
[[2, 'D'], [8, 'B'], [6, 'B']]
{'A': 0, 'B': 6, 'C': 1, 'D': 2, 'E': 5, 'F': inf}
[[5, 'E'], [8, 'B'], [6, 'B']]
{'A': 0, 'B': 6, 'C': 1, 'D': 2, 'E': 5, 'F': 7}
[[5, 'E'], [7, 'F'], [6, 'B'], [8, 'B']]
{'A': 0, 'B': 6, 'C': 1, 'D': 2, 'E': 5, 'F': 6}
[[6, 'B'], [6, 'F'], [8, 'B'], [7, 'F']]
{'A': 0, 'B': 6, 'C': 1, 'D': 2, 'E': 5, 'F': 6}
"""

print(dijkstra(mygraph, 'A'))
"""
{'A': 0, 'B': 6, 'C': 1, 'D': 2, 'E': 5, 'F': 6}
"""
