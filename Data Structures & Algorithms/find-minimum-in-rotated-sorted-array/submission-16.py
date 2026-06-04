class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            # key: Could the first 2 in the entire array possibly be to my right (e.g., at Index 3)?
            if nums[mid] <= nums[r]:
                r = mid
            else:
                l = mid + 1

        return nums[l]
        
        