class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numSet = set(nums)
        maxCount = 0
        for num in nums:
            # the starting num
            if num - 1 not in numSet:
                count = 1
                while num in numSet:
                    maxCount = max(maxCount, count)
                    count += 1
                    num += 1

        return maxCount
        