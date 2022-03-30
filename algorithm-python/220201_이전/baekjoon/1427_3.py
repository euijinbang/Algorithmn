# 0부터 9까지의 리스트를 만들어놓고
# 입력값을 돌면서 큰 수(리스트의 인덱스 끝부터)부터 확인하고 그 수가 등장하면 바로 프린트한다.

# count 세거나 따로 int list 만들 필요 없음!

board = [0] * 10
data = input()

for i in range(9, -1, -1):
    for j in data:
        if int(j) == i:      # 문자열을 정수로 바꿔준
            print(i, end='')
