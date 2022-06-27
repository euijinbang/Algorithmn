"""
6485. 삼성시의 버스 노선
<< Memoization (배열, 수학) >>

-방법0 (best)
정류장 미리 계산
1. 길이 5000인 배열
2. 각 원소에 출발 및 도착 카운트 0, 0으로 초기화
3. 노선 돌면서 출발, 도착점 카운트 증가
4. n 정류장 노선수
= n-1 정류장 출발 노선
+ n 정류장 출발 노선수
- n-1 정류장 도착 노선

-방법1
1. 모든 노선 체크 - 각 버스정류장마다 노선 돌면서 범위구간이면 cnt 증가


-방법2
1. 길이 5000인 배열 만들어둔다.
2. 노선 돌면서 1이상에서 3이하라면 배열 1, 2, 3에 카운트 증가
"""

T = int(input())


for tc in range(1, T+1):
    N = int(input())    # 버스 노선 수

    start = [0] * 5001  # 출발 정류장 표시
    end = [0] * 5001    # 도착 정류장 표시
    bus_stop = [0] * 5001   # 계산한 버스 표시

    for i in range(N):
        s, e = map(int, input().split())
        start[s] += 1
        end[e] += 1

    for i in range(len(bus_stop)-1):
        bus_stop[i+1] = bus_stop[i] - end[i] + start[i+1]

    P = int(input())   # 확인하고 싶은 정류장의 개수
    print("#{}".format(tc), end=" ")
    for _ in range(P):
        C = int(input())
        print(bus_stop[C], end=" ")
    print()  # 다음 테스트 케이스 위해 추가!