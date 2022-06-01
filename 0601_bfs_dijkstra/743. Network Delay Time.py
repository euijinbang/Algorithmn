class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        1. 인접리스트를 만든다. 이때 시작노드 : [(간선비용, 도착노드)]
        2. 최소힙에 간선비용과 시작점을 넣는다. 방문처리할 set도 만든다.
        3. 최소힙이 존재하는 동안 반복한다.
            1. 간선비용이 가장 작은 것부터 힙에서 꺼내 방문한다.
                이 때, 모든 노드를 방문했다면 간선비용을 리턴하고 함수를 종료한다.
            2. 이후 연결된 노드중에서 방문하지 않은 노드라면 간선비용이 작은 순서대로 힙에 넣는다.
                이 때, 현재 노드의 간선비용 + 현재 노드에서 힙에 넣을 노드까지의 간선비용을 더한다.
        """
        # 1. 인접리스트 만들기
        adj_list = collections.defaultdict(list)
        for u, v, w in times:
            adj_list[u].append((w, v)) # 시작노드 : [(간선비용, 도착노드)]

        # 2. 최소힙과 방문처리 세팅
        # minHeap 만든다(파이썬의 기본힙). 이때 (간선비용=0, 시작점) 넣는다.
        min_heap = [(0, k)]
        visited = set()

        while min_heap:
            travel_time, node = heapq.heappop(min_heap) # 비용 작은 것부터 꺼낸다!
            visited.add(node)   # 꺼내고 방문체크

            if len(visited) == n:
                return travel_time

            for time, adj_node in adj_list[node]:
                if adj_node not in visited:
                    heapq.heappush(min_heap, (travel_time + time, adj_node))

        return -1