class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            stack = list(str(x))
        else:
            stack = ['-'] + list(str(-x))

        i = 0
        while i <= len(stack) // 2:
            if stack[i] == stack[len(stack)-i-1]:
                i += 1
            else:
                return False
        return True
