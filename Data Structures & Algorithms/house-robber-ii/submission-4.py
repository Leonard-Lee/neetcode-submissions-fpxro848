class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]

        n = len(nums)
        # key: (idx, end), val: max money
        dp = {}
        # input: current idx and the end idx
        # output: the maximum money
        def dfs(idx: int, end: int) -> int:
            if idx > end:
                return 0

            if (idx, end) in dp:
                return dp[(idx, end)] 

            # not pick
            res = dfs(idx + 1, end)

            # pick
            dp[(idx, end)] = max(res, nums[idx] + dfs(idx + 2, end))

            return dp[(idx, end)]

        res = dfs(0, n - 2)
        return max(res, dfs(1, n - 1))
        