# all(배열) => 배열요소 모두 True여야 True
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        seen = [False] * len(rooms)

        def dfs(node):
            for adj in rooms[node]:
                if seen[adj] == False:
                    seen[adj] = True
                    dfs(adj)

        seen[0] = True
        dfs(0)

        return all(seen)

# set => 집합 - 집합
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        all_rooms = {x for x in range(len(rooms))}
        visited = set()

        def dfs(node):
            for adj in rooms[node]:
                if adj not in visited:
                    visited.add(adj)
                    dfs(adj)

        visited.add(0)
        dfs(0)

        return not(all_rooms - visited)
