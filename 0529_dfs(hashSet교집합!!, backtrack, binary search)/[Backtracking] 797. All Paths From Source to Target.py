class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        result = []
        visited = set()

        def backtrack(node, route):
            if node == len(graph)-1:
                result.append(route.copy())
                return

            for adj in graph[node]:
                if adj not in visited:
                    visited.add(adj)
                    route.append(adj)
                    backtrack(adj, route)
                    visited.remove(adj)
                    route.pop()

        visited.add(0)
        backtrack(0, [0])

        return result