import itertools
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
for x in itertools.combinations(members, 2):
    combs.append(list(x))

K = len(combs)
min_diff = 987654321
for i in range(K):
    scoreA, scoreB = 0, 0
    teamA, teamB = combs[i], combs[K-1-i]

    for r in range(N):
        for c in range(N):
            nums = len(teamA)
            score_combs_A = []
            score_combs_B = []

            for y in itertools.permutations(teamA, nums):
                score_combs_A.append(list(y))

            for y in itertools.permutations(teamB, nums):
                score_combs_B.append(list(y))

            for p in range(len(score_combs_A)):
                scoreA += data[score_combs_A[p][0]][score_combs_A[p][1]]

            for p in range(len(score_combs_B)):
                scoreB += data[score_combs_B[p][0]][score_combs_B[p][1]]

            diff = abs(scoreA - scoreB)
            min_diff = min(diff, min_diff)

print(min_diff)
