class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def binarySearch(nums: List[int], target: int) -> int:
            l, r = 0, len(nums) 
            while l < r:
                mid = (l + r) // 2
    
                if nums[mid] >= target: 
                    r = mid
                else:
                    l = mid + 1

            return l

        start = binarySearch(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]

        return [start, binarySearch(nums, target + 1) - 1]
        