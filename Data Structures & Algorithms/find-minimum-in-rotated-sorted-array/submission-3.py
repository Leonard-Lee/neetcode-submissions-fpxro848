class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums: 
            return -1
        elif len(nums) == 1:
            return 0

        l, r = 0, len(nums) - 1
        # we cannot use l <= r because it will cause infinite loop
        while l < r:
            m = l + ((r - l) // 2)
            # focus on the left part for the cut
            # we need to include m because right side is behaving well and m could be the smallest
            if nums[m] < nums[r]:
                r = m
            else:
                # focus on the right part; nums[m] already is the biggest in the right part
                # exclude it 
                l = m + 1
        return nums[l]
        