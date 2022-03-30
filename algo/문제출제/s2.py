import sys
sys.stdin = open('input_s.txt')

# T = int(input())

N, K = map(int, input().split())
# print(N, K)

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
# print(arr)


h = 0 # 작은삼각형(전구 밝기범위)의 높이
t = 0
for i in range(1, K+1):
    t += i
    h += 1
    if t == K:
        break

result = 0
for i in range(N-h+1):
    for j in range(i+1):
        total = arr[i][j]  # 꼭짓점의 위치

        t = 1
        while t < h:
            for l in range(j, j+t+1):
                total += arr[i+t][l]
            t += 1

        if total > result:
            result = total

print(result)