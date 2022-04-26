# DP : 잘게 쪼개서 작은 것부터 해결해나간다

# n, m = 4, 4
# arr = [[0, 1, 0, 0], [0, 1, 1, 1], [1, 1, 1, 0], [0, 0, 1, 0]]
# arr = [[0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
"""
누적합으로 정사각형 찾기
"""
n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            dp[i][j] = arr[i][j]
        elif arr[i][j] == 0:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

        answer = max(dp[i][j], answer)

print(dp)
print(answer * answer)

# 틀린풀이.. 이유는 모르겠다
maxNum = 0
for i in range(n):
    for j in range(m):
        # 1인 경우
        if arr[i][j] == 1:
            # 좌, 상, 좌상 중 최소인 수 + 1로 교체한다.
            arr[i][j] = min(arr[i-1][j], arr[i][j-1], arr[i-1][j-1]) + 1
            if arr[i][j] > maxNum:
                maxNum = arr[i][j]

print(arr)
print(maxNum * maxNum)

# 4 4
# 0111
# 0111
# 0111
# 1010

# 4 4
# 0100
# 0111
# 1110
# 0010

# 4 4
# 1000
# 0000
# 0000
# 0001

