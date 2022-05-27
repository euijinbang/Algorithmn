class Solution:
    def numberOfSteps(self, num: int) -> int:
        def toZero(n,cnt):
            if n == 0:
                return cnt
            else:
                if n % 2:
                    return toZero(n-1, cnt+1)
                else:
                    return toZero(n//2, cnt+1)

        return toZero(num,0)