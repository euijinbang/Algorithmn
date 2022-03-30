"""
정렬 알고리즘
counting sort
"""
import sys

n = 8
data = [1, 3, 2, 6, 4, 2, 5, 3]

# 수의 범위는 1 ~ 10000
counts = [0] * 10001

for i in range(n):
    counts[data[i]] += 1

for i in range(1, 10001):
    for _ in range(counts[i]):
        print(i)
