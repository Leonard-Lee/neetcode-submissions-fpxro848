class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []

        for i, num in enumerate(nums):
            left, right = i + 1, len(nums) - 1
            if i > 0 and nums[i - 1] == num: continue
            while left < right:
                three_sum = num + nums[left] + nums[right]
                if three_sum == 0:
                    ret.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]: 
                        left += 1

                elif three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1

        return ret


        