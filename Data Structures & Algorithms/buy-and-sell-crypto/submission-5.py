class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for price1 in prices:
            for later_price in prices[prices.index(price1):]:
                if later_price - price1 > max_profit:
                    max_profit = later_price - price1
        return max_profit
        