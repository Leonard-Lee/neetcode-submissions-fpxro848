class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        ret = [1] * len(nums)
        for i in range(len(nums)):
            ret[i] = product
            product *= nums[i]

        product = 1
        for i in range(len(nums) - 1, -1, -1):
            ret[i] *= product
            product *= nums[i]
            
        return ret

        