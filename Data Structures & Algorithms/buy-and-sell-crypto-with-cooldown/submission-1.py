class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        idx = 0
        isBuying = True
        cache = {} # key is (idx, isBuying): val is max profit

        def dfs(idx, isBuying):
            if idx >= len(prices):
                return 0

            if (idx, isBuying) in cache:
                return cache[(idx, isBuying)]

            if isBuying:
                buy = dfs(idx + 1, False) - prices[idx]
                cooldown = dfs(idx + 1, True)
                cache[(idx, isBuying)] = max(buy, cooldown)
            else:
                sell = dfs(idx + 2, True) + prices[idx]
                cooldown = dfs(idx + 1, False)
                cache[(idx, isBuying)] = max(sell, cooldown)
        
            return cache[(idx, isBuying)]

        return dfs(0, True)