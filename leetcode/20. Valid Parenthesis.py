def isValid(s):
    left = ['(', '[', '{']
    right = [')', ']', '}']

    stack = []

    for data in s:
        if not stack and data in right:
            return False

        for idx, l in enumerate(left):
            if data == l:
                stack.append(('l', idx))
        for idx, r in enumerate(right):
            if data == r:
                if idx == stack[-1][1] and stack[-1][0] == 'l':
                    stack.pop()
                else:
                    stack.append(('r', idx))

    if stack:
        return False
    else:
        return True

print(isValid("([}}])"))