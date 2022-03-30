import sys
sys.stdin = open("1966.txt")

# 배열에서 최댓값을 구한다.
# 맨 앞에 최댓값이 올때까지 큐를 돌린다.
# 맨 앞에 최댓값이 오면 카운트를 1 증가시킨다. 그 값이 타겟이면 카운트를 반환하고 종료한다.
# 뺀 값이 타겟이 아니면 그 다음 인덱스부터 위의 단계를 반복한다.

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    q = list(map(int, input().split(' ')))
    q = [(i, idx) for idx, i in enumerate(q)]

    count = 0
    while True:
        if q[0][0] == max(q, key=lambda x: x[0])[0]:  # key를 기준으로 q에서 최댓값을 찾는다.
            count += 1
            if q[0][1] == m:
                print(count)
                break
            else:
                q.pop(0)
        else:
            e = q.pop(0)
            q.append(e)

