class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        nums.sort()

        res = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            target = -num
            l = i + 1
            r = len(nums) - 1

            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append([nums[l], nums[r], num])
                    l += 1
                    r -= 1
                    
                    while l < len(nums) and nums[l - 1] == nums[l]:
                        l += 1
    
                    
                    while r >= 0 and nums[r] == nums[r + 1]:
                        r -= 1
        
        return res