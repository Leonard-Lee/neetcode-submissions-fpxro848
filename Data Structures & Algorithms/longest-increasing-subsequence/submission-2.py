class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return 1

        dp = {}

        def dfs(preIdx, idx) -> int:
            if idx == len(nums):
                dp[(preIdx, idx)] = 0
                return dp[(preIdx, idx)]
            elif (preIdx, idx) in dp:
                return dp[(preIdx, idx)]

            if preIdx == -1 or nums[preIdx] < nums[idx]:
                pick = 1 + dfs(idx, idx + 1)
                skip = dfs(preIdx, idx + 1)
                dp[(preIdx, idx)] = max(pick, skip)

            else:
                dp[(preIdx, idx)] = dfs(preIdx, idx + 1)

            return dp[(preIdx, idx)] 

        return dfs(-1, 0)
