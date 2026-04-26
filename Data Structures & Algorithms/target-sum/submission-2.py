class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 1D solution
        dp = defaultdict(int)
        dp[0] = 1

        for i in range(len(nums)):
            next_dp = defaultdict(int)

            for cur_sum, count in dp.items():
                next_dp[cur_sum + nums[i]] += dp[cur_sum]
                next_dp[cur_sum - nums[i]] += dp[cur_sum]

            dp = next_dp
        return dp[target]



        # 2D solution
        # # offset for zero items row
        # dp = [defaultdict(int) for i in range(len(nums) + 1)]
        # # zero items => key: sum is 0 and val is 1 (num of the ways)
        # dp[0][0] = 1

        # for i in range(len(nums)):
        #     for cur_sum, count in dp[i].items():
        #         dp[i + 1][cur_sum + nums[i]] += dp[i][cur_sum]
        #         dp[i + 1][cur_sum - nums[i]] += dp[i][cur_sum]

        # return dp[len(nums)][target]

        