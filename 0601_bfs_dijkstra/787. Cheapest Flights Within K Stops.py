class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        1. adj_list 만들기
        2. min heap pq 셋팅
        3. 노드 방문 총횟수를 저장할 vis 배열 세팅
        4. 다익스트라
            - 가장 간선비용이 작은 노드 pop
            - 노드 == 도착점이면 w 리턴
            - vis[node] >= k 면 k횟수를 넘어간 루트이므로 다음 노드로 넘어간다
            - vis[node] = k 해당 노드에 이용가능한 남은 k를 넣는다.
            - 연결된 주변노드 돌면서 가중치는 더하고 k-1 하여 힙에 저장한다.
        """

        #1.flights[i] = [fromi, toi, pricei]
        adj_list = collections.defaultdict(dict)
        for s, e, w in flights:
            adj_list[s][e] = w

        #2.weght, from, k+1
        min_heap = [(0, src, k+1)]

        #3.
        vis = [0] * n

        while min_heap:
            w, node, left_k = heapq.heappop(min_heap)
            if node == dst:
                return w

            if vis[node] >= left_k: # @@@@@pruning@@@@@
                continue

            vis[node] = left_k

            for adj, adj_w in adj_list[node].items():
                heapq.heappush(min_heap, (w+adj_w, adj, left_k-1))

        return -1
            