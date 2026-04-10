class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # 1. find the normal max
        preSum = nums[0]
        maxSum = nums[0]
        for i in range(1, len(nums)):
            preSum = max(preSum + nums[i], nums[i])
            maxSum = max(maxSum, preSum)

        # 2. total - min
        sum = 0
        for num in nums:
            sum += num

        preSum = nums[0]
        minSum = nums[0]
        for i in range(1, len(nums)):
            preSum = min(preSum + nums[i], nums[i])
            minSum = min(minSum, preSum)

        if sum == minSum:
            return maxSum
        return max(maxSum, sum - minSum)
        