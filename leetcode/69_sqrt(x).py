class Solution:
    """
    binary search를 통해
    제곱근 값을 구한다.
    """
    def mySqrt(self, x: int) -> int:
        # binary search
        left = 1
        right = x

        if x < 2:
            return x

        while left < right:
            mid = left + math.floor((right-left)/2)
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            elif mid * mid > x:
                right = mid

        return left - 1
