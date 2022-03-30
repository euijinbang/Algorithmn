# 시간 초과 문제 => sys.stdin.readline() 로 변경
# 메모리 초과 문제 => for 문 생략

import sys

n = int(sys.stdin.readline())

# 수의 범위 1 ~ 10000
counts = [0] * 100001

for i in range(n):
    counts[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
    for _ in range(counts[i]):
        print(i)




# import sys
# sys.stdin = open("10989.txt")
#
# # 메모리 초과
# # sys.stdin.readline()
#
# import sys
# n = int(input())
#
# data = []
# for _ in range(n):
#     data.append(int(sys.stdin.readline()))
#
# # 수의 범위 1 ~ 10000
# counts = [0] * 100001
#
# for i in range(n):
#     counts[data[i]] += 1
#
# for i in range(1, n):
#     counts[i] = counts[i] + counts[i-1]
#
# # data = [5, 2, 3, 1, 4, 2, 3, 5, 1, 7]
# # counts = [0, 2, 4, 6, 7, 9, 9, 10, 10, 10,...](누적)
#
# temp = [0] * n
#
#
# for i in range(n-1, -1, -1):
#     temp[counts[data[i]]-1] = data[i]
#     counts[data[i]] -= 1
#
# # data[9] 는 7이다. counts[7] = 10이다. 따라서 7까지 누적한게 10이므로 10번째(temp idx 9)는 7이다.
#
# for i in range(n):
#     print(temp[i])