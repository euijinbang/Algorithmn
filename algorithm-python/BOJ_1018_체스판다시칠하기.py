import sys
sys.stdin = open("1018.txt")

"""
W, B 경우를 나누어 각각의 횟수를 카운팅하는 것이 문제 해결을 솔루션이다.
또한 특정 칸의 인덱스 i 와 j의 합을 2로 나눈 경우 짝수인지, 홀수인지로 위치가 결정된다.
"""

N, M = map(int, input().split())

arr = []
count_list = []

for _ in range(N):
    arr.append(input())

for i in range(N - 7):
    for j in range(M - 7):
        index1 = 0  # 'W'로 시작할 경우 바뀐 체스 판의 개수
        index2 = 0  # 'B'로 시작할 경우 바뀐 체스 판의 개수
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if arr[a][b] != 'W':
                        index1 += 1
                    if arr[a][b] != 'B':
                        index2 += 1
                else:
                    if arr[a][b] != 'B':
                        index1 += 1
                    if arr[a][b] != 'W':
                        index2 += 1

        count_list.append(min(index1, index2))

print(min(count_list))



