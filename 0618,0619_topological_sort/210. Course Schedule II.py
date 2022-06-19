class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        WHITE: 방문 안한 상태
        GRAY : 방문은 했고 stack 에 추가는 안한 상태
        BLACK: 방문도 했고 인접노드가 없어서 stack에 추가한 상태
        """

        WHITE = 1
        GRAY = 2
        BLACK = 3

        # 1. 그래프 생성: [A, B] B가 A에 선행되어야 하므로 B에서 A로 가는 엣지를 만든다.
        graph = collections.defaultdict(list)

        for dest, src in prerequisites:
            graph[src].append(dest)

        stack = [] # 차례로 담아 나중에 거꾸로 출력
        is_possible = True # cycle이면 False

        color = {k: WHITE for k in range(numCourses)} # key는 노드, val = 1로 세팅

        def dfs(v):
            nonlocal is_possible

            # cycle 존재시 함수종료
            if not is_possible:
                return

            # 방문처리
            color[v] = GRAY

            for adj in graph[v]:
                if color[adj] == WHITE:
                    dfs(adj)
                elif color[adj] == GRAY: #cycle
                    is_possible = False

            # no more adj nodes to process. Recursion ends
            color[v] = BLACK
            stack.append(v)


        # 0부터 n-1까지 for로 돈다. dfs가 돌다가 완료되면 다음 노드부터 다시 시작한다.
        for i in range(numCourses):
            if color[i] == WHITE:
                dfs(i)

        return stack[::-1] if is_possible else []


        