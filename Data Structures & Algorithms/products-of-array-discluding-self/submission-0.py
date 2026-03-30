class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        prefix = [0] * len(nums)
        for i in range(len(nums)):
            prefix[i] = product
            product *= nums[i]

        product = 1
        postfix = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            postfix[i] = product
            product *= nums[i]
            
        ret = [0] * len(nums)
        for i in range(len(nums)):
            ret[i] = prefix[i] * postfix[i]

        return ret

        