import sys
sys.stdin = open("5397.txt")

t = int(input())

# 반례는 어디에..

def get_password(data):
    stack = []
    temp = []

    for key in data:
        if len(stack) == 0:
            if key.isalpha():
                stack.append(key)
            else:
                pass
        else:
            if key == '<':
                if len(stack) == 0:
                    pass
                else:
                    temp.append(stack.pop())

            elif key == '>':
                if len(temp) == 0:
                    pass
                else:
                    stack.append(temp.pop())

            elif key.isalpha() or key.isnumeric():
                stack.append(key)

            else:
                if len(stack) == 0:
                    pass
                else:
                    stack.pop()

    stack.extend(temp[::-1])

    return ''.join(stack)



for _ in range(t):
    data = input()
    result = get_password(data)
    print(result)


