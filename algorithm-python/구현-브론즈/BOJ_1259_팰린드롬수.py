"""
구현-브론즈
"""
import sys

sys.stdin = open("../input_1259.txt")


def isPalindrome(data):
    if len(data) % 2:
        if data[:len(data) // 2] == data[len(data) // 2 + 1:][::-1]:
            return True
    else:
        if data[:len(data) // 2] == data[len(data) // 2:][::-1]:
            return True

    return False


while True:
    numStr = input()
    if numStr == '0':
        break

    # string to int-list
    arr = [int(x) for x in numStr]
    ans = isPalindrome(arr)
    if ans:
        print('yes')
    else:
        print('no')
