class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        # [3,4,5,6,1,2]
        #  0 1 2 3 4 5
        # l = 0 3 3 4
        # r = 5 5 4 4
        #mid= 2 4 3
        return nums[l]
        