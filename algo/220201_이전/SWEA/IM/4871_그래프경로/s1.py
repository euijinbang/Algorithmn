import sys
sys.stdin = open('input.txt')

def check_route(graph, V, start, end):
    """
        그래프의 시작 노드부터 도착 노드까지 경로가 있는지 확인한다.
    :param graph: 경로 그래프(2차원 배열의 인접 행렬)
    :param V: 그래프의 노드의 개수
    :param start: 시작 노드
    :param end: 도착 노드
    :return: 경로가 있다면 True, 없다며 False를 리턴한다.
    """

    # 스택에 시작점을 넣고 시작한다.
    stack = [start]
    visited = [False] * (V+1)

    # 스택이 빌 때까지 반복한다
    while stack:
        # 현재 스택을 꺼내 현재값에 할당한다.
        now = stack.pop()
        visited[now] = 1

        for next in range(1, V+1):
            # 현재 노드와 연결되어 있고 아직 방문하지 않은 노드라면
            if graph[now][next] and not visited[next]:
                # 도착 노드라면 True를 반환한다.
                if next == end:
                    return True
                # 도착 노드가 아니라면 갈 수 있는 곳이므로 스택에 추가한다.
                stack.append(next)
    # 출발 노드에서 시작하여 탐색을 종료했지만 도착 노드에 방문하지 않았다면 Fals를 반환한다.
    return False

T = int(input())

for tc in range(1, T+1):
    # V : 노드의 갯수 / E : 간선의 개수
    V, E = map(int, input().split())
    # graph: 그래프의 경로를 나타내는 인접행렬
    graph = [[0] * (V + 1) for _ in range(V+1)]

    for _ in range(E):
        start, end = map(int, input().split())
        graph[start][end] = 1

    S, G = map(int, input().split())

    result = int(check_route(graph, V, S, G))
    print("#{} {}".format(tc, result))