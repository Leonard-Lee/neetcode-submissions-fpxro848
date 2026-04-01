class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        checkDuplicateSet = set(nums)
        max_length = 0
        for num in nums:
            if num - 1 not in checkDuplicateSet:
                cur = num
                length = 1
                while cur + 1 in checkDuplicateSet:
                    cur += 1
                    length += 1
                    max_length = max(max_length, length)
        return max_length

            
        