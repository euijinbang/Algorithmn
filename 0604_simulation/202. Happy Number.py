class Solution:
    def isHappy(self, n: int) -> bool:
        """
        set()으로 사이클을 확인한다.

        """

        # 19 -> 1**2 + 9**2 = 82
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        # cycle 확인을 위한 seen "hashSet"
        seen = set()

        # n이 1이라면 중단, 사이클 생기면 중단
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        # n이 1이면 True를, 1이 아니면 False를 반환한다.
        return n == 1