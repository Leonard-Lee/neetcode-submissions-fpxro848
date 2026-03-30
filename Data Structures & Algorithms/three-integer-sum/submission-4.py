class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3: return []

        nums.sort()
        ret = []
        for i, num in enumerate(nums):
            # skip the next one if the next one has the same value
            if i > 0 and num == nums[i - 1]: continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = num + nums[l] + nums[r] 
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    ret.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while (l < r and nums[l - 1] == nums[l]):
                        l += 1
        return ret

        