class Solution:
    def longestValidParentheses(self, s: str) -> int:

        # 1. BRUTE FORCE
        #         def is_valid(s):
        #             stack = []
        #             for char in s:
        #                 if char == "(":
        #                     stack.append(char)
        #                 elif stack and char == ")" and stack[-1] == "(":
        #                     stack.pop()
        #                 else:
        #                     return False
        #             return stack == []

        #         max_len = 0
        #         for i in range(0, len(s)-1, 1):
        #             for j in range(i+2, len(s)+1, 2):
        #                 if is_valid(s[i:j]):
        #                     max_len = max(max_len, j-i)

        #         return max_len

        # 2. INDEX IN STACK
        max_len = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:   # ")" 라서 pop했는데 스택이 비어있다면 인덱스를 넣는다.
                    stack.append(i)
                else:   # ")" 라서 pop했는데 스택이 남아있다면 () 이므로 길이를 갱신한다.
                    max_len = max(max_len, i - stack[-1])

        return max_len