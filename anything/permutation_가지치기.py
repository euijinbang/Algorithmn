"""
순열을 만들기
1부터 N까지 모든 순열 만들기
N = 3

1, 2, 3의 순열은 1, 2, 3중 3개를 뽑아 나열하는 것이다.

visited 가지치기를 하지 않으면 111 112 113 ... 모든 수가 중복된다.
가지치기 하면 매 depth 마다 앞에서 뽑은 수가 나오면 건너뛴다.
"""
N = 3
visited = [0] * (N + 1)


def permute(start, perm):
    if len(perm) == N:
        print(perm)
        return

    for i in range(start, N + 1):
        if visited[i] == 1:
            continue

        perm.append(i)
        visited[i] = 1
        permute(start, perm)
        perm.pop()
        visited[i] = 0


permute(1, [])
