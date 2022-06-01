class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:

        # 1. 양방향 그래프 만들기
        graph = collections.defaultdict(list)

        for i in range(len(edges)):
            s, e = edges[i]
            graph[s].append((-succProb[i], e))  # max_heap 위한 음수 가중치
            graph[e].append((-succProb[i], s))

        # 2. max_heap 세팅 (음수가 들어가야함!)
        max_heap = [(-1, start)]
        visited = set()

        # 3. 다익스트라
        while max_heap:
            p, node = heapq.heappop(max_heap)  # p < 0

            # 종료조건
            if node == end:
                return -p

            visited.add(node)

            for q, adj in graph[node]:
                if adj not in visited:
                    heapq.heappush(max_heap, (-(p*q), adj))

        return 0
