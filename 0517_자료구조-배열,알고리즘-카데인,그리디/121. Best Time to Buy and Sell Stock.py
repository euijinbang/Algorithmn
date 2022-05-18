"""
카데인 알고리즘
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 카데인 알고리즘
        max_profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit
