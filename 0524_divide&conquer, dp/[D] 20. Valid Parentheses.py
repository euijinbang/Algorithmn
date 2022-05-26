class Solution:
    def isValid(self, s: str) -> bool:
        # @return a boolean
        stack = []
        d = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in d.values():
                stack.append(char)
            elif char in d:
                if not stack or d[char] != stack.pop():
                    return False
        return not stack    # stack에 요소가 남아있으면 False
