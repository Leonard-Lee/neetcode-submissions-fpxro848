class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # trick is all the numbers are positive. So it's been visited, we make it negative
        # for i in range(len(nums)):
        #     print("i: " + str(i))
        #     print("num: " + str(nums[i]))
        #     if nums[nums[i] - 1] >= 0:
        #         nums[i] *= -1
        #     else:
        #         return nums[i] 
        # return 0


        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1
            else:
                return abs(num)
        return 0
        