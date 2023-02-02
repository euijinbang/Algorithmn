class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        if src == dst: return 0

        # seen == 시작점에서 i 위치까지 도달하는 최소 거리
        d, seen = collections.defaultdict(list), collections.defaultdict(lambda: float('inf'))
        for u, v, p in flights:
            d[u] += [(v, p)]

        q = [(src, -1, 0)]

        while q:
            pos, k, cost = q.pop(0)

            # 뽑은 값의 k(시작점에서 pos까지 거쳐온 노드 수)
            # 가 K와 같으면 더 이상 진행하지 않는다.
            if pos == dst or k == K: continue
            for nei, p in d[pos]:
                if cost + p >= seen[nei]:
                    continue
                else:
                    seen[nei] = cost+p
                    q += [(nei, k+1, cost+p)]

        return seen[dst] if seen[dst] < float('inf') else -1