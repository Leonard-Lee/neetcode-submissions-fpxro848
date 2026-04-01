class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # trick is all the numbers are positive. So it's been visited, we make it negative
        for i in range(len(nums)):
            if nums[nums[i] - 1] > 0:
                nums[i] *= -1
            else:
                return nums[i] 
        return 0
        