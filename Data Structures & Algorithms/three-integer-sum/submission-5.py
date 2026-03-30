class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3: return []

        nums.sort()
        ret = []
        # [-1,0,1,2,-1,-4]
        # sorted -> [-4, -1, -1, 0, 1, 2]
        #             0, 1.   2  3  4  5
        # num = -1
        #.  i = 1, l = 2, r =5
        #   i = 1, l = 3, r=4
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = num + nums[l] + nums[r]
                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    ret.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return ret


        