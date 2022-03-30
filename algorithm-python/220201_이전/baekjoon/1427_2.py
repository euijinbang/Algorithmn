# 0부터 9까지의 리스트를 만들어놓고
# 입력값을 모두 돌면서 큰 수(리스트의 인덱스 끝부터)부터 확인하고 그 수가 등장하면 1을 추가한다.
# 한 번 돌고 나면 그 수(인덱스)를 등장 횟수만큼 출력한다.

board = [0] * 10
data = input()
arr = list()
for d in data:
    arr.append(int(d))

n = len(arr)
for i in range(9, -1, -1): # i는 9부터 0까지
    for j in range(0, n): # j는 0부터 n-1까지
        if arr[j] == i:
            board[i] += 1

    if board[i] >= 1:
        for _ in range(board[i]):
            print(i, end='')               # board[i] (등장 횟수)만큼 출력

