class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        # adj list 생성
        tickets.sort()  # 정렬
        adj = collections.defaultdict(list)
        for src, dest in tickets:
            adj[src].append(dest)

        route = ["JFK"]
        def dfs(src):
            if len(route) == len(tickets) + 1:
                return True
            if src not in adj:  # backtrack - 도착지 없는 티켓 제외
                return False

            tmp = list(adj[src])
            for i, v in enumerate(tmp):
                adj[src].pop(i)
                route.append(v)

                if dfs(v): return True

                adj[src].insert(i, v)
                route.pop()

            return False

        dfs("JFK")

        return route