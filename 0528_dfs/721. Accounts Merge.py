# set 활용한 버젼
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        # 1. graph(set!)
        graph = collections.defaultdict(set)
        mail_to_name = {}

        for account in accounts:
            name = account[0]
            for mail in account[1:]:
                graph[mail].add(account[1])
                graph[account[1]].add(mail)
                mail_to_name[mail] = name

        # 2. dfs
        def dfs(node_mail):
            for adj_mail in graph[node_mail]:
                if adj_mail not in visited:
                    visited.add(adj_mail)
                    route.append(adj_mail)
                    dfs(adj_mail)

        # mail돌면서 연결끝나면 결과업데이트
        result = []
        visited = set()
        for node_mail in graph:
            route = []
            if node_mail not in visited:
                visited.add(node_mail)
                route.append(node_mail)
                dfs(node_mail)

            if route:
                result.append([mail_to_name[node_mail]] + sorted(route))

        return result







class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        accounts.sort()

        # 1. graph
        graph = collections.defaultdict(list)

        for account in accounts:
            name = account[0]
            for mail in account[1:]:
                if len(account[1:]) >= 2:
                    for other in account[1:]:
                        if mail != other:
                            graph[name, mail].append(other)
                else:
                    graph[name, mail].append(mail)

        # 2. dfs
        def dfs(name, node_mail):
            for adj_mail in graph[name, node_mail]:
                if adj_mail not in visited:
                    visited.add(adj_mail)
                    route.append(adj_mail)
                    dfs(name, adj_mail)

        # mail돌면서 연결끝나면 결과업데이트
        semi_result = []
        visited = set()
        print(graph)
        for name, node_mail in graph:
            route = []
            person_info = []
            if node_mail not in visited:
                visited.add(node_mail)
                route.append(node_mail)
                dfs(name, node_mail)

            route.sort()
            person_info.append(name)
            person_info.extend(route)

            semi_result.append(person_info)

        result = [x for x in semi_result if len(x) >= 2]
        return result
