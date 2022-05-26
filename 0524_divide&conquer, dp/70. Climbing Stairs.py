class Solution:
    dp = collections.defaultdict(int)
    def climbStairs(self, n: int) -> int:
        # 재귀풀이(점화식) => 시간초과
        # f(n) = f(n-2) + f(n-1)

        # if n <= 2: return n
        # return self.climbStairs(n-2) + self.climbStairs(n-1)


        # dp - memoization
        if n <= 2: return n
        if self.dp[n]: return self.dp[n]

        self.dp[n] = self.climbStairs(n-2) + self.climbStairs(n-1)
        return self.dp[n]

        # dp - one, two 활용
        # n = 5
        # [0, 0, 0, 1, 1]
        #          one two
        # [0, 0, 2, 1, 1]
        #       one two
        # [0, 3, 2, 1, 1]
        #    one two
        # [5, 3, 2, 1, 1]
        # one two
        one, two = 1, 1
        for i in range(n-1):
            tmp = one
            one = two + one
            two = tmp
        return one
