mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

import heapq


# 시작 정점에서 다른 정점까지의 최단거리와 최단경로
def dijkstra(graph, start, end):
    # 1. initialize distances
    distances = {node: [float('inf'), start] for node in graph}  # node 별로 value를 inf 로 초기화
    distances[start] = [0, start]

    # 2. initialize heap-queue
    queue = []
    heapq.heappush(queue, [distances[start][0], start])

    print(distances)    # {'A': [0, 'A'], 'B': inf, 'C': inf, 'D': inf, 'E': inf, 'F': inf}
    print(queue)    # [[0, 'A']]

    # 3. start logics
    # until queue exists
    while queue:
        # 3-1. pop data(with the highest priority) from heapq
        current_distance, current_node = heapq.heappop(queue)  # [0, 'A']

        # 3-2. if distances is less than current_distance : continue
        if distances[current_node][0] < current_distance:
            continue

        # 3-3. else, check adjs
        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adjacent][0]:
                distances[adjacent] = [distance, current_node]
                heapq.heappush(queue, [distance, adjacent])

                print(distances)
                print(queue)

    path = end
    path_output = end + '->'
    while distances[path][1] != start:
        path_output += distances[path][1] + '->'
        path = distances[path][1]
    path_output += start
    print(path_output)

    return distances


"""
distances
queue

{'A': [0, 'A'], 'B': [inf, 'A'], 'C': [inf, 'A'], 'D': [inf, 'A'], 'E': [inf, 'A'], 'F': [inf, 'A']}
[[0, 'A']]
{'A': [0, 'A'], 'B': [8, 'A'], 'C': [inf, 'A'], 'D': [inf, 'A'], 'E': [inf, 'A'], 'F': [inf, 'A']}
[[8, 'B']]
{'A': [0, 'A'], 'B': [8, 'A'], 'C': [1, 'A'], 'D': [inf, 'A'], 'E': [inf, 'A'], 'F': [inf, 'A']}
[[1, 'C'], [8, 'B']]
{'A': [0, 'A'], 'B': [8, 'A'], 'C': [1, 'A'], 'D': [2, 'A'], 'E': [inf, 'A'], 'F': [inf, 'A']}
[[1, 'C'], [8, 'B'], [2, 'D']]
{'A': [0, 'A'], 'B': [6, 'C'], 'C': [1, 'A'], 'D': [2, 'A'], 'E': [inf, 'A'], 'F': [inf, 'A']}
[[2, 'D'], [8, 'B'], [6, 'B']]
{'A': [0, 'A'], 'B': [6, 'C'], 'C': [1, 'A'], 'D': [2, 'A'], 'E': [5, 'D'], 'F': [inf, 'A']}
[[5, 'E'], [8, 'B'], [6, 'B']]
{'A': [0, 'A'], 'B': [6, 'C'], 'C': [1, 'A'], 'D': [2, 'A'], 'E': [5, 'D'], 'F': [7, 'D']}
[[5, 'E'], [7, 'F'], [6, 'B'], [8, 'B']]
{'A': [0, 'A'], 'B': [6, 'C'], 'C': [1, 'A'], 'D': [2, 'A'], 'E': [5, 'D'], 'F': [6, 'E']}
[[6, 'B'], [6, 'F'], [8, 'B'], [7, 'F']]
"""

print(dijkstra(mygraph, 'A', 'F'))
"""
F->E->D->A
{'A': [0, 'A'], 'B': [6, 'C'], 'C': [1, 'A'], 'D': [2, 'A'], 'E': [5, 'D'], 'F': [6, 'E']}

"""
