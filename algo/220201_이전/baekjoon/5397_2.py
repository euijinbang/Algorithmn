import sys

sys.stdin = open("5397.txt")

t = int(input())


def get_password(data):
    # left | cursor | right

    left_stack = []
    right_stack = []

    for key in data:
        if key == '-':
            if left_stack:
                left_stack.pop()

        elif key == '<':
            if left_stack:
                right_stack.append(left_stack.pop())

        elif key == '>':
            if right_stack:
                left_stack.append(right_stack.pop())

        else:
            left_stack.append(key)

    left_stack.extend(right_stack[::-1])

    return ''.join(left_stack)


for _ in range(t):
    data = input()
    result = get_password(data)
    print(result)