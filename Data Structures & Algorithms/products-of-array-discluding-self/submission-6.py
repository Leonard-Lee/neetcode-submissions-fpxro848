class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        preProducts = 1
        # [1, 1, 2, 8]
        for i in range(len(nums)):
            res[i] = preProducts
            preProducts *= nums[i]

        preProducts = 1
        # [1, 1, 2, 8]
        # [ 48,   24,  12, 8]
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= preProducts
            preProducts *= nums[i]

        return res
        