class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        numSet = set(nums)
        maxCount = 1

        for num in nums:
            count = 1
            while num + 1 in numSet:
                count += 1
                maxCount = max(maxCount, count)
                num += 1

        return maxCount
        