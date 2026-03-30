class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate_set = set()
        for num in nums:
            if num in duplicate_set:
                return True
            duplicate_set.add(num)
        return False
        