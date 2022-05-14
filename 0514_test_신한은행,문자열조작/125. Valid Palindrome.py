"""
성능 우수한 순
시간복잡도 : 3 > 2 > 1
공간복잡도 : 3 > 1 > 2
"""

from collections import deque
class Solution:
    def isPalindrome(self, s: str) -> bool:

        # 1. 문자열 + two pointer
        new = ''
        for data in s:
            if data.isalnum():
                new += data.lower()
        l, r = 0, len(new)-1

        while l < r:
            if new[l] != new[r]:
                return False
            l += 1
            r -= 1
        return True

        # 2. deque
        strs = deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True

        # 3. 정규식 + slicing
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]
