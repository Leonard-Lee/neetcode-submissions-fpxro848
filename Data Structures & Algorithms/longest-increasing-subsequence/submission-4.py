class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # return the max length in the current idx
        dp = {}
        def dfs(preIdx, idx) -> int:
            if (preIdx, idx) in dp:
                return dp[(preIdx, idx)]
            
            if idx == len(nums):
                return 0

            # not pick up
            skip = dfs(preIdx, idx + 1)

            include = 0
            if preIdx == -1 or nums[preIdx] < nums[idx]:
                include = 1 + dfs(idx, idx + 1)

            dp[(preIdx, idx)] = max(skip, include)
            return dp[(preIdx, idx)]

        return dfs(-1, 0)
        