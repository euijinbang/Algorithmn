class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Sliding window
        # l = buying, r = selling
        # memory : no array -> O(1), time : O(n)

        l, r = 0, 1
        maxProfit = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
                r += 1

        return maxProfit



        # 시간초과
#         maxProfit = 0
#         for i in range(n-1):
#             for j in range(i + 1, n):
#                 if prices[j] > prices[i]:
#                     profit = prices[j] - prices[i]
#                     maxProfit = max(profit, maxProfit)

#         return maxProfit