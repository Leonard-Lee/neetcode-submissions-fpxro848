class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # offset for zero items row
        dp = [defaultdict(int) for i in range(len(nums) + 1)]
        # zero items => key: sum is 0 and val is 1 (num of the ways)
        dp[0][0] = 1

        for i in range(len(nums)):
            for cur_sum, count in dp[i].items():
                dp[i + 1][cur_sum + nums[i]] += dp[i][cur_sum]
                dp[i + 1][cur_sum - nums[i]] += dp[i][cur_sum]

        return dp[len(nums)][target]

        