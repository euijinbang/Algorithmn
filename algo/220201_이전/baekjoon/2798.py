import sys
sys.stdin = open("2798.txt")

N, M = map(int, input().split(' '))
data = list(map(int, input().split(' ')))

# 카드는 각 한장씩만 있음에 주의!!

result = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum_value = data[i] + data[j] + data[k]
            # if sum_value > M:
            #     pass
            # else:
            #     if sum_value > max:
            #         max = sum_value
            if sum_value <= M:
                result = max(result, sum_value)  # 더 큰 값이 반환된다.

print(result)
