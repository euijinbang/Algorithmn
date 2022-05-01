#1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
#1. 아이디어 - backtracking
#2. 시간복잡도 - 중복 없으므로 N!
#3. 자료구조 - 방문여부 확인배열, 선택값 입력배열
#N이 10 언저리면 backtracking

N, M = 4, 2


#res길이로 base case 결정
res = []
visited = []
def backtracking(res):
    if len(res) == M:
        print(' '.join(map(str, res)))
        return
    for n in range(1, N+1):
        if n not in visited:
            visited.append(n)
            res.append(n)
            backtracking(res)
            res.pop()
            visited.pop()
backtracking(res)


#depth로 base case 결정
res = []
visited = [False] * (N+1)
def backtracking(depth):
    if depth == M:
        print(' '.join(map(str, res)))
        return
    for n in range(1, N+1):
        if visited[n] == False:
            visited[n] = True
            res.append(n)
            backtracking(depth+1)
            visited[n] = False
            res.pop()
backtracking(0)