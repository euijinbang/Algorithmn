class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # [10, 15, 20]
        # sol1. 인덱스 앞에서 뒤로...
        dp = collections.defaultdict(int)
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-2], dp[i-1]) + cost[i]

        return min(dp[len(cost)-1], dp[len(cost)-2])

        # sol2. 인덱스 뒤에서 앞으로... i는 1, 0(2는 고정)
        # [10, 15, 20, 0]
        cost.append(0)
        for i in range(len(cost)-3, -1, -1):
            cost[i] = min(cost[i+2], cost[i+1]) + cost[i]

        return min(cost[0], cost[1])
