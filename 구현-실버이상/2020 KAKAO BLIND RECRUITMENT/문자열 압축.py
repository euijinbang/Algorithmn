"""
갯수가 12일 경우 1, 2 이렇게 두 자리로 친다.
"""

def solution(s):
    data = list(s)
    N = len(data)
    answer = 1001
    count = 1
    for i in range(1, N + 1):
        visited = [0] * N
        new_data = []

        for j in range(0, N, i):
            if visited[j] == 1:
                continue

            tmp = data[j:j+i]

            for k in range(j, j+i):
                if j+i < N:
                    visited[k] = 1

            if sum(visited) == N:
                break

            count = 1
            for s in range(j+i, N, i):
                next = data[s:s+i]
                if tmp == next:
                    count += 1
                    for q in range(s, s+i):
                        visited[q] = 1
                else:
                    if count != 1:
                        new_data.extend(list(str(count)))
                        new_data.extend(tmp)
                    else:
                        new_data.extend(tmp)
                    break

        if count != 1:
            new_data.extend(list(str(count)))
            new_data.extend(tmp)
        else:
            new_data.extend(tmp)

        if len(new_data) < answer:
            answer = len(new_data)

    return answer


print(solution("aaaaaaaaaaaabcd"))

