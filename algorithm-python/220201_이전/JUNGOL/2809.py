import sys
sys.stdin = open("input.txt")

from math import sqrt

N = int(input())

ans = []
for i in range(1, int(sqrt(N))+1):
# for i in range(1, int(N ** 0.5)+1):
    if N % i == 0:
        ans.append(i)
        if N // i != i:      # 10 * 10 = 100인 경우 중복
            ans.append(N // i)
ans.sort()
for num in ans:
    print(num, end=' ')
