class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i, j = 0, n - 1

        while i < j:
            if nums[i] & 1 == 1 and nums[j] & 1 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -=1
            elif nums[i] & 1 == 0:
                i += 1
            else:
                j -= 1
        
        return nums
        