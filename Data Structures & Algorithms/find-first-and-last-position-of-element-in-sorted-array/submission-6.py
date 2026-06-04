class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        n = len(nums)

        # key: Lower-Bound Pattern
        def binarySearch(target):
            l = 0
            r = n

            while l < r:
                mid = (l + r) // 2

                if target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1

            return l

        start = binarySearch(target)
        if start == n or nums[start] != target:
            return [-1, -1]

        return [start, binarySearch(target + 1) - 1]
        