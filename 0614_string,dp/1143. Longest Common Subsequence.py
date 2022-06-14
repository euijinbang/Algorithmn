class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        DP
            a b c d e
          0 0 0 0 0 0
        a 0 1 1 1 1 1
        c 0 1 1 2 2 2
        e 0 1 1 2 2 3

        """

        # m x n
        m, n = len(text1), len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    # max of left & upper value
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

        return dp[m][n]
    