import sys
sys.stdin = open("input.txt")

N = int(input()) # 주어지는 명령의 갯수

stack = []

for _ in range(N):
    order = input()
    if order.startswith('i'):
        ord, num = order.split()
        stack.append(num)
    if order == 'o':
        if stack:
            print(stack.pop())
        else:
            print("empty")
    elif order == 'c':
        print(len(stack))





