from collections import deque

n, k = map(int, input().split())


def josephus(n, k):
    q = deque()
    answer = []

    for i in range(1, n+1):
        q.append(i)

    while q:
        for j in range(k-1):
            q.append(q.popleft())
        answer.append(q.popleft())

    return answer


result = josephus(n, k)

print("<", end="")
for i in range(len(result)-1):
    print(result[i], end=", ")
print(result[-1], end="")
print(">")

