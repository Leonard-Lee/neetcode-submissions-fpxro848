class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # i means front pointer and j means back pointer
        i, j = 0, 0
        while j < n:
            if nums[j] % 2 == 1:
                break
            j += 1

        while i < n and j < n:
            if nums[i] % 2 == 0:
                i += 1
            elif nums[j] % 2 == 1:
                j += 1
            else:
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i] 
                    i += 1
                    j += 1

        return nums

        # [4,2,5,7]
        # i = 0, 1, 2
        # [3,1,2,4]
        # i = 0, 
        # j = 1

        # is it possible that i >= j?
        # [2,2,2,1]
        # i = 0,1,2,3
        # j = 1
        