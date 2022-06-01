class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        avail_city = {}
        graph = collections.defaultdict(list)

        #1. 양방향 graph 만듦
        for s, e, w in edges:
            graph[s].append((w, e))
            graph[e].append((w, s))

        #2. 각 출발지마다 계산
        for i in range(n):
            avail_city[i] = set()
            pq = [(0, i)]
            visited = set()

            while pq:
                w, node = heapq.heappop(pq)

                # pruning
                if node in visited: # 이미 방문한 경우 진행하지 않는다.
                    continue

                if node != i:   #조건 달면 더 빨라진다.add연산 줄어드니까.
                    visited.add(node)

                for dw, adj in graph[node]:
                    # 조건: w+dw가 Threshold 보다 작거나 같으면 city에 node담고 이동, 크면 패스
                    # 이미 방문한 경우 더이상 진행하지 않음(가지치기)
                    if adj not in visited and adj != i and w+dw <= distanceThreshold:
                        avail_city[i].add(adj)   # start city에 담기
                        heapq.heappush(pq, (w+dw, adj))

        # 3. avail_city 돌면서 value길이가 가장 작은 city 구하고 그중 최댓값 리턴
        min_len = min([len(x) for x in avail_city.values()])
        max_city = 0
        for sc, ec in avail_city.items():
            if len(ec) == min_len:
                max_city = max(sc, max_city)

        return max_city