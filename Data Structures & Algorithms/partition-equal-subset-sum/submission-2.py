class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 == 1:
            return False

        target = total // 2
        dp = {}

        def dfs(idx, curSum) -> bool:
            if (idx, curSum) in dp:
                return dp[(idx, curSum)]

            if curSum > target:
                dp[(idx, curSum)] = False
                return False
            elif curSum == target:
                dp[(idx, curSum)] = True
                return True
            elif idx == len(nums):
                dp[(idx, curSum)] = False
                return False

            # not pick
            skip = dfs(idx + 1, curSum)

            # pick
            included = dfs(idx + 1, curSum + nums[idx])

            dp[(idx, curSum)] = skip or included
            return dp[(idx, curSum)]

        return dfs(0, 0)
        