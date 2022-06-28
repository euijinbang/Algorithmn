"""
5432. 쇠막대기 자르기
<< stack >>

1. (  => 스택에 항상 추가
2. )  => 스택에서 ( 일단 제거
- 리스트에서 ) 이전이 ( 라면 레이저이므로 쌓여있던 스택 수만큼 추가
- 리스트에서 ) 이전이 ) 라면 막대 끝이므로 몸통개수 +1

"""

T = int(input())

for tc in range(1, T+1):
    sticks = list(input())
    stack = []
    cnt = 0
    for i, stick in enumerate(sticks):
        if stick == "(":
            stack.append(stick)
        if stick == ")":
            stack.pop()
            if sticks[i-1] == "(":
                cnt += len(stack)
            if sticks[i-1] == ")":
                cnt += 1

    print("#{} {}".format(tc, cnt))
