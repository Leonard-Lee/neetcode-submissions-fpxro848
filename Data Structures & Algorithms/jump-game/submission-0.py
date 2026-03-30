class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums: 
            return False
        elif len(nums) == 1:
            return True

        length = len(nums)
        goal = length - 1
        for i in range(length - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0


        
        