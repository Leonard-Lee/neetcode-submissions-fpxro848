class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0

        for num in nums:
            if num:
                product *= num
            else:
                zero_count += 1
        
        ret = [0] * len(nums)
        if zero_count == 1:
            for i, num in enumerate(nums):
                if num == 0: ret[i] = product
            return ret 
        else:
            for i, num in enumerate(nums):
                ret[i] = product // num

        return ret


        