from collections import deque

n, k = map(int, input().split())


def josephus(n, k):     # n명의 사람들이 원으로 앉아있을 때, k번째 사람부터 kill~
    q = deque()
    answer = []

    for i in range(1, n+1):
        q.append(i)

    while q:
        for j in range(k-1):        # k-1 번 만큼 앞에서 빼서 뒤로 보낸다.
            q.append(q.popleft())
        answer.append(q.popleft())  # 답에 맨 앞의 수를 빼서 넣는다.

    return answer


result = josephus(n, k)

print("<", end="")
for i in range(len(result)-1):
    print(result[i], end=", ")
print(result[-1], end="")
print(">")

