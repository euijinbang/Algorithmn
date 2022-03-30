# N = 5
# data = [(55, 185), (58, 183), (88, 186), (60, 175), (46, 155)]
"""
1차시도 fail (소요시간 40분이상)
해결방법
- 인덱스를 활용하여 자신보다 몸무게와 키가 모두 큰 사람 수를 구해 + 1 해주면 끝!
- 따로 정렬할 필요 없다.
"""
N = int(input())
data = []
for i in range(N):
    x, y = map(int, input().split())
    data.append((x, y))

ranks = []
for i in range(N):
    count = 0   # 사람이 바뀔때 마다 본인보다 덩치가 큰 사람의 수를 초기화한다
    for j in range(N):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:    # 몸무게와 키 모두 본인보다 큰 사람의 수를 센다
            count += 1
    ranks.append(count + 1)  # 덩치 등수는 자신보다 몸무게, 키가 모두 큰 사람의 수 + 1

for rank in ranks:
    print(rank)

