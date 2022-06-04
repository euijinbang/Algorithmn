class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        """
        다익스트라 알고리즘은 시작 노드에서 도착 노드까지의 최소거리를 찾는다.
        ++변형(DP)

        times 배열 : src -> dst까지의 최소 소요시간을 구한다.
        ways 배열 : src -> dst까지 가는 (최소 거리의) 방법의 수

        1. adj_list 를 생성한다.(bidirectional)   # node, time
        2. times, ways 배열을 초기화한다. times[0] = 0, ways[0] = 1
        3. pq를 세팅한다.   # [(t, u)]
        4. 다익스트라를 돌면서, pop한 현재노드와 연결된 노드가
            4-1. 미래노드까지의 예상거리가 현재 times[미래노드] 보다 작으면
            해당 시간과 노드를 힙에 추가
            소요시간을 갱신
            ways를 갱신(현재노드까지의 ways로)

            4-2. 미래노드까지의 예상거리가 현재 times[미래노드] 와 같으면
            소요시간 갱신필요 x, 해당 미래노드를 대기열에 넣을 필요x (중복되는 거리이므로
            해당 미래노드로 굳이 갈 이유가 없다.)
            *** ways만 현재노드까지의 ways 를 더해 갱신한다.

        4. 다 돌고나면 ways[dst] 를 반환한다.
        """


        #1. graph
        graph = collections.defaultdict(list)
        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))

        #2. times, ways array initializer
        times = [float('inf')] * n
        ways = [0] * n

        times[0] = 0
        ways[0] = 1

        #3. dijkstra
        pq = [(0, 0)] # time, node

        while pq:
            old_t, u = heapq.heappop(pq) # current time, current node

            for v, t in graph[u]:
                new_t = old_t + t

                # casual logic: update shorter path
                if new_t < times[v]:
                    times[v] = new_t
                    ways[v] = ways[u]
                    heapq.heappush(pq, (new_t, v))

                # if find same time path... update ways only
                elif new_t == times[v]:
                    ways[v] += ways[u]

        modulo = 10 ** 9 + 7

        return ways[n-1] % modulo
