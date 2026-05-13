class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numSet = set(nums)
        maxCount = 1

        for num in nums:
            if num - 1 not in numSet:
                count = 1
                while num + 1 in numSet:
                    count += 1
                    num += 1
                maxCount = max(maxCount, count)

        return maxCount
        