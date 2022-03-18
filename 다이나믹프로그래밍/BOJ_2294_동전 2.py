n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

# coins = [2, 3, 5]
# n, k = 3, 7
d = [10001] * (k + 1)
d[0] = 0
for i in range(n):
    for j in range(coins[i], k + 1):  # 2원이라면 2원부터 k원까지
        # 새롭게 가격을 만드는 방법이 존재하는 경우
        if d[j-coins[i]] != 10001:    # 0원부터 바텀업
            d[j] = min(d[j-coins[i]] + 1, d[j])

if d[k] == 10001:
    print(-1)
else:
    print(d[k])


