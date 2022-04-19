# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        result = n

        while left <= right:
            mid = (left + right) // 2

            # mid가 불량품이면 result 갱신 (더 작은 수이므로), 최우측 = mid-1
            if isBadVersion(mid):
                result = mid
                right = mid - 1

            # mid가 불량품이 아니면 최좌측 = mid + 1
            else:
                left = mid + 1

        return result
