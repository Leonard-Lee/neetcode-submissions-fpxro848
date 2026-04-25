class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {} # key is (idx, sum) val is the num of ways
        def backtrack(idx, sum):
            if (idx, sum) in dp:
                return dp[(idx, sum)]

            if idx == len(nums):
                return 1 if sum == target else 0

            dp[(idx, sum)] = backtrack(idx + 1, sum + nums[idx]) + backtrack(idx + 1, sum - nums[idx]) 
            return dp[(idx, sum)]

        return backtrack(0, 0)
        