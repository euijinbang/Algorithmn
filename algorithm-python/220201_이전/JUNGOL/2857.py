import sys
sys.stdin = open("input.txt")

# 이 부분때문에 accept(30) 뜸. 각 줄의 시작과 마지막에 빈칸은 없다. => 고 했는데.. 아닌것같다.
arr = []
max_col = 0
for row in range(5):
    r = list(input())
    arr.append(r)
    if len(r) > max_col:
        max_col = len(r)

# 가운데 있으면 빈 문자열로 들어오는데, 끝이 비면 안들어옴 => 뒤가 모자라는 경우 빈 문자열로 처리
for row in arr:
    row.extend([" "] * (max_col - len(row)))

answer = ''
for i in range(max_col):
    for j in range(5):
        # 문자열에 공백만 있으면 true 를 반환
        if arr[j][i] == ' ':
            pass
        else:
            answer += arr[j][i]

print(answer)

