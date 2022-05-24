class Solution:
    dp = collections.defaultdict(int)

    def fib(self, n: int) -> int:
        # sol1. 일반 재귀
        if n <= 1:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)

        # sol2. dp-memoization => ***fastest
        if n <= 1:
            return n

        if self.dp[n]:  # 한번 계산했던 수는 바로 결과값을 리턴(3, 2)
            return self.dp[n]
        self.dp[n] = self.fib(n-2) + self.fib(n-1)
        return self.dp[n]

        # sol3. dp-tabulation
        self.dp[0] = 0
        self.dp[1] = 1

        for i in range(2, n+1):
            self.dp[i] = self.dp[i-1] + self.dp[i-2]

        return self.dp[n]
