import sys
sys.stdin = open("14501.txt")

# DP
# t: 일을 완료하는데 걸리는 기간, p: 일을 완료하면 받을 수 있는 금액
# d[n] 은 n+1일에 받을 수 있는 최대 금액

n = int(input())

t = [0]
p = [0]
d = [0] * (n+2)
result = 0

for i in range(n):
    a, b = map(int, input().split(' '))
    t.append(a)
    p.append(b)

for i in range(1, n+2):
    for j in range(1, i):
        if j + t[j] == i:
            d[i] = max(d[i], d[j] + p[j])
        else:
            d[j] = max(d[i], d[j])

    result = max(result, d[i])

print(result)
