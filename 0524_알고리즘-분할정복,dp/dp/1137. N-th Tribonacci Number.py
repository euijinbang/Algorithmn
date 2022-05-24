class Solution:
    dp = collections.defaultdict(int)
    def tribonacci(self, n: int) -> int:


        # dp - tabulation
        memo = defaultdict(int)
        memo[0], memo[1], memo[2] = 0, 1, 1
        for i in range(3, n+1):
            memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
        return memo[n]


        # dp - recursion(memoization)
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 1

        if self.dp[n]: return self.dp[n]
        self.dp[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)

        return self.dp[n]