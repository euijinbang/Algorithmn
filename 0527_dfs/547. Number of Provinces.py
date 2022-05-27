class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m, n = len(isConnected), len(isConnected[0])

        # 1. 양방향 그래프 만들기, isolated 위해서 빈 리스트 만들어지도록 한다.
        graph = {node : [] for node in range(n)}
        for i in range(m):
            for j in range(n):
                if isConnected[i][j] == 1 and i < j:
                    graph[i].append(j)
                    graph[j].append(i)


        # dfs 해당 노드의 인접노드 중 방문하지 않은 노드가 있다면 방문처리하고
        # 다음 노드로 이동한다.
        def dfs(node):
            for adj in graph[node]:
                if adj not in visited:
                    visited.add(adj)
                    dfs(adj)


        # 2. 그래프 순회하면서 연결된 섬의 갯수를 센다.
        # 방문하지 않았다면 방문처리하고 province 갯수를 증가시킨다.
        provinces = 0
        visited = set()
        for node in graph:
            if node not in visited:
                provinces += 1
                visited.add(node)
                dfs(node)

        return provinces