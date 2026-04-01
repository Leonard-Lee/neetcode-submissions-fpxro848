class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums: return 0

        l, r = 0, len(nums) - 1
        while True:
            if l + 1 == r:
                return min(nums[l], nums[r])
            m = l + ((r - l) // 2)
            # focus on the left part for the cut
            if nums[m] < nums[r]:
                r = m
            else:
                # focus on the right part
                l = m
        