
T = int(input())

for tc in range(1, T+1):
    N = int(input())    # 버스 노선 수

    bus_stop = [0] * 5001   # 계산한 버스 표시

    for i in range(N):
        s, e = map(int, input().split())
        for j in range(s, e+1):
            bus_stop[j] += 1

    P = int(input())   # 확인하고 싶은 정류장의 개수
    print("#{}".format(tc), end=" ")
    for _ in range(P):
        C = int(input())
        print(bus_stop[C], end=" ")
    print()  # 다음 테스트 케이스 위해 추가!