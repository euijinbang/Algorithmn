class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window, 중복을 피하기 위한 hashSet사용
        #중복원소가 나오면 좌측을 하나 올린다. 매번 최대길이 갱신
        #l, r 인덱스 사용

        #방법1. hashSet 사용
        l = 0
        res = 0
        charSet = set()

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            charSet.add(s[r])
            res = max(res, r - l + 1)

        return res

        #방법2. hashMap사용
        l = 0
        res = 0
        charMap = {}

        for r in range(len(s)):
            while s[r] in charMap:
                del charMap[s[l]]
                l += 1

            charMap[s[r]] = r
            res = max(res, r - l + 1)

        return res