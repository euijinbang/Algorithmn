import sys
sys.stdin = open("input.txt")

N = int(input()) # 주어지는 명령의 갯수

queue = []

for _ in range(N):
    order = input()
    if order.startswith('i'):
        ord, num = order.split()
        queue.append(num)
    elif order.startswith('c'):
        print(len(queue))
    else:

        if queue:
            print(queue.pop(0))
        else:
            print('empty')