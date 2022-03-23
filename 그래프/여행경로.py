"""
풀이 by. by-gramm
- 티켓 => 노드를 단방향으로 연결
- 딕셔너리 형식으로 티켓정보(공항 연결정보)와 visited 를 확인
- 공항에 연결된 공항(티켓 도착장소) 이 있으면 방문, 다음 공항을 방문...
- 주어진 티켓을 모두 사용하면 True를 리턴, 경로가 없다면 False를 리턴
- 경로가 없다면 routes에서 pop 해서 연결된 다른 공항을 탐색
"""


def find_route(count, current):
    """
    Args:
        count: 현재까지 사용한 티켓의 개수
        current: 현재 탐색중인 공항

    Returns:
        경로를 찾은 경우 True, 아닌 경우 False
    """
    # 주어진 티켓을 모두 사용한 경우
    if count == ticket_count:
        return True

    # [["ICN", "AAA"], ["ICN", "BBB"], ["BBB", "ICN"]] => ["ICN", "BBB", "ICN", "AAA"]
    # 현재 공항에서 출발하는 경로가 없는 경우
    if current not in airports:
        return False

    for i in range(len(airports[current])):
        if not visited[current][i]:
            airport = airports[current][i]
            routes.append(airport)
            visited[current][i] = True

            # 모든 티켓을 사용하는 경로를 찾은 경우
            if find_route(count + 1, airport):
                return True

            routes.pop()
            visited[current][i] = False

    # 모든 티켓을 사용하는 경로를 찾지 못한 경우
    return False


def solution(tickets):
    global airports, ticket_count, routes, visited

    airports = dict()            # key: 시작 공항 / value: 도착 공항 리스트
    ticket_count = len(tickets)  # 총 티켓 개수
    routes = ['ICN']             # 알파벳 순서로 가장 앞서는 경로
    visited = dict()             # key: 시작 공항 / value: 도착 공항 방문 여부 리스트

    for start, end in tickets:
        if start not in airports:
            airports[start] = [end]
        else:
            airports[start].append(end)

    for start, ends in airports.items():
        visited[start] = [False] * len(ends)

    # 시작 공항별로 도착 공항을 알파벳 순으로 정렬한다.
    airports = {start: sorted(ends) for start, ends in airports.items()}

    print(airports)  # {'ICN': ['AAA', 'BBB'], 'BBB': ['ICN']}
    print(visited)   # {'ICN': [False, False], 'BBB': [False]}
    # 알파벳 순으로 가장 앞서는 경로를 routes에 저장한다.
    find_route(0, 'ICN')


    return routes


# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
tickets = [["ICN", "AAA"], ["ICN", "BBB"], ["BBB", "ICN"]]
print(solution(tickets))
