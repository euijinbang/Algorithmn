
T = int(input())

def bus_count(bus_stop):
    cnt = 0
    for i in range(N):
        if bus_routes[i][0] <= bus_stop <= bus_routes[i][1]:
            cnt += 1
    return cnt


for tc in range(1, T+1):
    N = int(input())    # 버스 노선 수
    bus_routes = []     # 버스의 노선을 저장해둘 리스트
    for _ in range(N):
        s, e = map(int, input().split())
        bus_routes.append((s, e))

    P = int(input())   # 확인하고 싶은 정류장의 개수
    ans = []        # 버스 수를 저장해 놓을 리스트
    for _ in range(P):
        C = int(input())
        ans.append(bus_count(C))

    print("#{}".format(tc), end=" ")
    print("{}".format(' '.join(map(str, ans))))
