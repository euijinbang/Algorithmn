import sys
sys.stdin = open("1874.txt")

# 스택에 원소를 삽입할 때는 특정 수에 도달할 때까지 삽입한다.
# 스택에서 원소를 연달아 뺄 때, 내림차순이 유지되지 않으면 연산이 불가하다.
n = int(input())

stack = []
result = []
count = 1

for i in range(n):
    data = int(input())

    while count <= data:    # 입력받은 데이터에 도달할 때 까지 삽입
        stack.append(count)
        count += 1
        result.append("+")

    if stack[-1] == data:   # 스택 최상위 원소가 데이터와 같을 때 출력
        stack.pop()
        result.append("-")

    else:
        print("NO")
        exit(0)     # 노 출력 후 프로그램 종료


print('\n'.join(result))    # 줄바꿈을 기준으로 출력




