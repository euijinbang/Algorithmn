import sys
sys.stdin = open('input_s.txt')

N, K = map(int, input().split())
arr = [0] * N

for i in range(N):
    arr[i] = list(map(int, input().split()))
    arr[i] += [0] * (N-i)


h = 0 # 작은삼각형(전구 밝기범위)의 높이
t = 0
for i in range(1, K+1):
    t += i
    h += 1
    if t == K:
        break

result = 0
for i in range(N-h+1):
    for j in range(N):
        total = 0
        if arr[i][j]:  # 0이 아닐때
            for k in range(h):
                for l in range(k+1):
                    total += arr[i+k][j+l]

            if total > result:
                result = total

print(result)
