graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

print(graph)


def bfs(graph, node):
    visited, need_to_visit = list(), list()

    need_to_visit.append(node)

    while need_to_visit:
        node = need_to_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_to_visit.extend(graph[node])

    print(visited)


bfs(graph, 'A')

def dfs(graph, node):
    visited, need_to_visit = list(), list()

    need_to_visit.append(node)

    while need_to_visit:
        node = need_to_visit.pop()
        if node not in visited:
            visited.append(node)
            need_to_visit.extend(graph[node])

    print(visited)


dfs(graph, 'A')
