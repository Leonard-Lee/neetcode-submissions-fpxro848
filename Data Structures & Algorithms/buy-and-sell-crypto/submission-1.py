class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l, r = 0, 1

        while l < len(prices) - 1 and r < len(prices):
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit, profit)
            if profit <= 0:
                l = r
                r = l + 1
            else:
                r += 1

        return maxProfit
            
        