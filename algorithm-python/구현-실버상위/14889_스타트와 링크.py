from itertools import combinations
import sys
# N = 4
# data = [
#     [0, 0, 0, 0, 0],
#     [0, 0, 1, 2, 3],
#     [0, 4, 0, 5, 6],
#     [0, 7, 1, 0, 2],
#     [0, 3, 4, 5, 0]
# ]

# 좌, 상 테두리 씌우기(인덱스 1부터 시작하도록)
N = int(sys.stdin.readline())
data = [[0]*(N+1)]
for _ in range(N):
    data.append([0] + list(map(int, sys.stdin.readline().split())))

members = [x+1 for x in range(N)]
combs = []
for x in combinations(members, N//2):
    combs.append(list(x))

#print(combs)  # [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
K = len(combs)
min_diff = 987654321
for i in range(K):
    scoreA, scoreB = 0, 0
    teamA, teamB = combs[i], combs[K-1-i]

    for i in range(0, N//2):
        for j in range(i+1, N//2):
            scoreA += data[teamA[i]][teamA[j]] + data[teamA[j]][teamA[i]]
            scoreB += data[teamB[i]][teamB[j]] + data[teamB[j]][teamB[i]]

    diff = abs(scoreA - scoreB)
    min_diff = min(diff, min_diff)

print(min_diff)
