class Solution:
    def coinChange(self, coins: List[int], target: int) -> int:
        dp = {} # key is (idx, amount) and val is min num of coins
        # def backtrack(idx, amount):
        #     if (idx, amount) in dp:
        #         return dp[(idx, amount)]

        #     if amount == target:
        #         return 0 # return num of coins
        #     elif amount > target or idx >= len(coins):
        #         return float("inf") 

        #     skip = backtrack(idx + 1, amount)
        #     include = 1 + backtrack(idx, amount + coins[idx])
        #     dp[(idx, amount)] = min(skip, include)
        #     return dp[(idx, amount)]

        # res = backtrack(0, 0)
        # return -1 if res == float("inf") else res

        def dfs(amount):
            if amount in dp:
                return dp[amount]

            if amount == 0:
                return 0
            elif amount < 0:
                return float("inf")

            res = float("inf")
            for coin in coins:
                res = min(res, 1 + dfs(amount - coin))

            dp[amount] = res
            return dp[amount]
        
        minCoins = dfs(target)
        return minCoins if minCoins != float("inf") else -1

        