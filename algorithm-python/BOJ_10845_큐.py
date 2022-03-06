"""
라이브러리 말고 리스트로 구현
"""


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


def main():
    # import sys
    # sys.stdin = open("BOJ_10845_input.txt")

    q_list = list()
    n = int(input())

    for i in range(n):
        order_list = input().split()
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
