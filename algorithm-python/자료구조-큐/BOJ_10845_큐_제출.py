"""
라이브러리 말고 리스트로 구현-브론즈
시간초과 -> sys.stdin.readline() 사용
"""
import sys


def push(ll, x):
    ll.append(x)


def pop(ll):
    if len(ll) != 0:
        print(ll[0])
        del ll[0]
    else:
        print(-1)


def size(ll):
    print(len(ll))


def empty(ll):
    if ll:
        print(0)
    else:
        print(1)


def front(ll):
    if len(ll) != 0:
        print(ll[0])
    else:
        print(-1)


def back(ll):
    if len(ll) != 0:
        print(ll[-1])
    else:
        print(-1)


q_list = list()
n = int(sys.stdin.readline())


def main():
    for i in range(n):
        order_list = sys.stdin.readline().split()
        order = order_list[0]

        if len(order_list) != 1:
            num = order_list[1]
            push(q_list, num)

        else:
            if order == "front":
                front(q_list)
            elif order == "back":
                back(q_list)
            elif order == "pop":
                pop(q_list)
            elif order == "size":
                size(q_list)
            else:  # empty
                empty(q_list)


if __name__ == "__main__":
    main()