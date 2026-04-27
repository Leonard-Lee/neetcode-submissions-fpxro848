class Solution:
    def coinChange(self, coins: List[int], target: int) -> int:
        dp = {} # key is (idx, amount) and val is min num of coins
        def backtrack(idx, amount):
            if (idx, amount) in dp:
                return dp[(idx, amount)]

            if amount == target:
                return 0 # return num of coins
            elif amount > target or idx >= len(coins):
                return float("inf") 

            skip = backtrack(idx + 1, amount)
            include = 1 + backtrack(idx, amount + coins[idx])
            dp[(idx, amount)] = min(skip, include)
            return dp[(idx, amount)]

        res = backtrack(0, 0)
        return -1 if res == float("inf") else res
        