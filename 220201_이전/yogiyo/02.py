import sys
sys.stdin = open("input.txt")

MAX = 2 ** 20 - 1
N = [str(x) for x in range(9)]

def solution(S):
    stack = []

    for s in list(S):

        if s in N:
            if int(s) > MAX:
                return False
            stack.append(s)

        elif s == "POP":
            if not stack:
                return False
            stack.pop()

        elif s == "DUP":
            if not stack:
                return False
            stack.append(stack[-1])

        elif s == "-":
            if len(stack) < 2:
                return False
            s1 = stack.pop()
            s2 = stack.pop()
            stack.append(int(s1)-int(s2))

        else:
            if len(stack) < 2:
                return False
            s1 = stack.pop()
            s2 = stack.pop()
            stack.append(int(s1)+int(s2))

    if not stack:
        return False

    return stack[-1]


print(solution(input().split()))

