class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = {}
        n = len(nums)
        dp[n] = (1, 1)
        globalMax = float("-inf")
        globalMin = float("inf")

        maxVal = 1
        minVal = 1

        for num in nums:
            preMax = maxVal
            maxVal = max(num * maxVal, num * minVal, num)
            minVal = min(num * preMax, num * minVal, num)
            # print("(" + str(maxVal) + ", " + str(minVal) + ")")

            globalMax = max(globalMax, maxVal)
            globalMin = min(globalMin, minVal)
            # print("(" + str(globalMax) + ", " + str(globalMin) + ")")
    
        return globalMax
        # def dfs(idx: int):
        #     nonlocal globalMax
        #     nonlocal globalMin

        #     if idx in dp:
        #         return dp[idx]

        #     nxtMax, nxtMin = dfs(idx + 1)
        #     maxVal = max(nums[idx] * nxtMax, nums[idx] * nxtMin, nums[idx])
        #     minVal = min(nums[idx] * nxtMax, nums[idx] * nxtMin, nums[idx])

        #     dp[idx] = (maxVal, minVal)
        #     globalMax = max(globalMax, maxVal)
        #     globalMin = min(globalMin, minVal)

        #     return dp[idx]

        # dfs(0)
        # return globalMax

            
        