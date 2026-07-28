class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:
        n = len(costs)

        # memo = {}
        # def dfs(idx) -> int:
        #     if idx in memo:
        #         return memo[idx]

        #     if idx <= 1:
        #         memo[idx] = 0
        #         return 0
            
        #     memo[idx] = min(dfs(idx - 2) + costs[idx - 2], dfs(idx - 1) + + costs[idx - 1]) 
        #     return memo[idx]

        # return dfs(n)
        memo = [0] * (n + 1)
        for i in range(2, n + 1):
            memo[i] = min(memo[i - 2] + costs[i - 2], memo[i - 1] + costs[i - 1])

        return memo[n]
        