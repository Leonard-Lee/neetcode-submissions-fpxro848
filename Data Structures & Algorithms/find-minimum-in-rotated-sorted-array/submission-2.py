class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        elif len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1
        while l < r:
            m = l + ((r - l) // 2)
            # focus on the left part for the cut
            if nums[m] < nums[r]:
                r = m
            else:
                # foＫcus on the right part
                l = m + 1
        return nums[l]
        