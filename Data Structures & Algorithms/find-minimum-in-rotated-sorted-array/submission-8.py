class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1

        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            # focus on the left part for the cut
            # we need to include m because right side is behaving well and m could be the smallest
            # think about [6, 1, 4]
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1

        return nums[l]
        